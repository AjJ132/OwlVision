import sqlalchemy as db
import pandas as pd
import random
from faker import Faker


fake = Faker()


def initial_data_setup():
    print("Starting initial data setup...")
    # Step 1

    #init postgresql database connection
    engine = db.create_engine(
                'postgresql+psycopg2://admin:password@localhost:5432/OwlVisionPrototype')

    # Gather data from general pool and put in session-table
    with engine.connect() as connection:
        print("Starting transfer for session table")
        #clear out session table
        connection.execute("DELETE FROM sessiontable;")
        connection.execute("INSERT INTO sessiontable SELECT * FROM generaluserpool;")

    # Copy Session table into Analytics table
    # TODO Add Analytics table

    total_count = 0

    # Gather total count of rows
    with engine.connect() as connection: 
        result = connection.execute("SELECT COUNT(*) FROM sessiontable;")
        total_count = result.fetchone()[0]
        print("Total count of rows: " + str(total_count))

    # Copy Random number of rows from session table into Merchandise buyers (1/4 of total count)
    grab_count = total_count / 4

    #add randomness to grab_count
    grab_count = random.randint(grab_count - 100, grab_count + 100)
    print("Grab count for merchandise table: " + str(grab_count))

    indices_to_remove = []

    #grab random rows from session table within the grab_count
    with engine.connect() as connection:
        print("Starting transfer for merchandise table")
        #reset merchandisebuyers table
        connection.execute("DELETE FROM merchandisebuyers;")

        #save data to pandas dataframe
        sessionDf = pd.read_sql_table('sessiontable', engine)
        
        #grab random rows
        merchandiseDf = sessionDf.sample(n=grab_count)

        #remove home_address column
        print("Removing home_address column from merchandise table")
        merchandiseDf = merchandiseDf.drop(columns=['home_address'])

        #loop over rows and add random merchandise data
        for index, row in merchandiseDf.iterrows():
            print(index)
            random_chance = random.random()

            # 80% chance to mark for removal
            if random_chance <= 0.8:
                indices_to_remove.append(merchandiseDf.at[index, 'id'])

            random_date = fake.date_between(start_date='-5y', end_date='today')

            # Convert the date object to a string in 'YYYY-MM-DD' format
            date_str = random_date.strftime('%Y-%m-%d')
            
            # Update the DataFrame
            merchandiseDf.at[index, 'purchasedate'] = date_str
            merchandiseDf.at[index, 'moneyspent'] = random.randint(0, 150)


        #save to merchandise table
        print("Saving merchandise table to database")
        merchandiseDf.to_sql('merchandisebuyers', con=engine,
                  if_exists='append', index=False)
        
        # From the dataframe remove 80% of the rows that were used in the merchandise table
        

        print("Removing merchandise rows from session table")
        sessionDf = sessionDf[~sessionDf['id'].isin(indices_to_remove)]
        #remove the rows from the session table
        sessionDf.to_sql('sessiontable', con=engine,
                  if_exists='replace', index=False)
        
        #print new count
        result = connection.execute("SELECT COUNT(*) FROM sessiontable;")
        total_count = result.fetchone()[0]
        print("New total count of rows: " + str(total_count))

        #clear dataframes
        sessionDf = None
        merchandiseDf = None

    return

    # Repeat for Mailing list table (1 / 6 of total count)
    with engine.connect() as connection:
        print("Starting transfer for mailing list table")
        #adjust total count
        result = connection.execute("SELECT COUNT(*) FROM sessiontable;")
        total_count = result.fetchone()[0]

        #adjust grab count
        grab_count = total_count / 6
        
        #save data to pandas dataframe
        df = pd.read_sql_table('sessiontable', engine)
        #grab random rows
        df = df.sample(n=grab_count)

        #save to mailinglist table
        df.to_sql('mailinglist', con=engine,
                  if_exists='append', index=False)
        
        # From the dataframe remove 80% of the rows
        df = df.sample(frac=0.2)

        #remove the rows from the session table
        df.to_sql('sessiontable', con=engine,
                  if_exists='replace', index=False)

    # Repeat for regular game attendance table ( 1/ 6 of total count)
    with engine.connect() as connection:
        print("Starting transfer for regular game attendance table")
        #adjust total count
        result = connection.execute("SELECT COUNT(*) FROM sessiontable;")
        total_count = result.fetchone()[0]

        #adjust grab count
        grab_count = total_count / 6
        
        #save data to pandas dataframe
        df = pd.read_sql_table('sessiontable', engine)
        #grab random rows
        df = df.sample(n=grab_count)

        #save to regularticketbuyers table
        df.to_sql('regularticketbuyers', con=engine,
                  if_exists='append', index=False)
        
        # From the dataframe remove 80% of the rows
        df = df.sample(frac=0.2)

        #remove the rows from the session table
        df.to_sql('sessiontable', con=engine,
                  if_exists='replace', index=False)
    

    # Repeat for parents of KSU students table (1 / 6 of total count)

    # Take the remaining 1/3 of the session table and copy into the alumni table


    # Step 2
    # Any remaining spread evenly across the other tables by random

    # Generate Analysis data from Analytics table
    # Need pie charts of each category, General trends, and a few other things TODO later

    # Data setup step complete

initial_data_setup()