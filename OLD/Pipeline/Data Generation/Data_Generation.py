import sqlalchemy as db
from sqlalchemy import text
import pandas as pd
import csv
from faker import Faker

fake = Faker()


def generate_data_and_save_to_database():
    try:
        data = []
        print("Generating general pool data...")
        for _ in range(4000):  # Generate 4000 entries for general pool
            entry = {
                'id': _,
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'phone_number': fake.phone_number(),
                'email': fake.email(),
                'home_address': fake.address().replace('\n', ', ')
            }
            data.append(entry)

        print("Saving general pool data to CSV...")
        keys = data[0].keys()
        with open('GeneralPool1.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

        groundTruthData = []
        print("Generating ground truth data...")
        for _ in range(300):  # Generate 100 entries for ground truth data
            entry = {
                'id': _,
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'phone_number': fake.phone_number(),
                'email': fake.email(),
                'home_address': fake.address().replace('\n', ', ')
            }
            groundTruthData.append(entry)

        print("Saving ground truth data to CSV...")
        keys = groundTruthData[0].keys()
        with open('GroundTruth.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(groundTruthData)

        print("Connecting to PostgreSQL...")
        engine = db.create_engine(
            'postgresql+psycopg2://admin:password@localhost:5432/OwlVisionPrototype')
        connection = engine.connect()

        print("Saving general pool data to SQL database...")
        #first clear the table
        connection.execute("DELETE FROM generaluserpool")
        
        df = pd.read_csv('GeneralPool1.csv')
        df.to_sql('generaluserpool', con=engine,
                  if_exists='replace', index=False)

        print("Saving ground truth data to SQL database...")
        #first clear the table
        connection.execute("DELETE FROM groundtruth")
        df = pd.read_csv('GroundTruth.csv')
        df.to_sql('groundtruth', con=engine, if_exists='replace', index=False)

        print("Closing database connection...")
        connection.close()

        print("Operation successful.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


# generate_data_and_save_to_database()
