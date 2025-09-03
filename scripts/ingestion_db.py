import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

# Setup logging
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# Connect to SQLite DB
engine = create_engine('sqlite:///inventory.db')

# Ingest small/normal CSV
def ingest_db(df, table_name):
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

# Ingest large CSV in chunks (e.g. >100MB)
def ingest_large_csv(csv_path, table_name, chunksize=100_000):
    for i, chunk in enumerate(pd.read_csv(csv_path, chunksize=chunksize)):
        mode = 'replace' if i == 0 else 'append'
        chunk.to_sql(table_name, con=engine, if_exists=mode, index=False)
        logging.info(f"{table_name}: inserted chunk {i+1}")

# Main ingestion logic
def load_raw_data():
    start_all = time.time()
    folder = 'data'

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        # Handle only .csv (case-insensitive) files
        if file.lower().endswith('.csv') and not file.startswith('~'):
            file_clean = file.strip()
            table_name = file_clean.rsplit('.', 1)[0].strip()

            try:
                size_mb = os.path.getsize(file_path) / (1024 * 1024)
                start = time.time()

                logging.info(f"Ingesting {file_clean} ({size_mb:.2f} MB) into '{table_name}'")

                if size_mb > 100:
                    ingest_large_csv(file_path, table_name)
                else:
                    df = pd.read_csv(file_path)
                    ingest_db(df, table_name)

                duration = time.time() - start
                logging.info(f"✅ Finished {table_name} in {duration:.2f} sec")

            except Exception as e:
                logging.error(f"❌ Error ingesting {file_clean}: {e}")
    
    total_time = (time.time() - start_all) / 60
    logging.info("---------- Ingestion complete ----------")
    logging.info(f"🕒 Total time taken: {total_time:.2f} minutes")

# Backup ingestion for vendor_invoice.csv
def ensure_vendor_invoice():
    try:
        path = 'data/vendor_invoice.csv'
        if os.path.exists(path):
            df = pd.read_csv(path)
            ingest_db(df, 'vendor_invoice')
            logging.info("✅ Manually ingested vendor_invoice.csv")
            print("✅ Manually ingested vendor_invoice.csv")
        else:
            logging.warning("⚠️ vendor_invoice.csv not found in data/")
    except Exception as e:
        logging.error(f"❌ Failed to ingest vendor_invoice.csv: {e}")
        print(f"❌ Error: {e}")

# Run
if __name__ == '__main__':
    load_raw_data()
    ensure_vendor_invoice()




