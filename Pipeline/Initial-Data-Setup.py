import pandas as pd



def initial_data_setup():
    # Step 1

    #init postgresql database connection
    engine = db.create_engine(
                'postgresql+psycopg2://admin:password@localhost:5432/OwlVisionPrototype')

    # Gather data from general pool and put in session-table
    with engine.connect() as connection:
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

    #grab random rows from session table within the grab_count
    with engine.connect() as connection:
        #save data to pandas dataframe
        df = pd.read_sql_table('sessiontable', engine)
        #grab random rows
        df = df.sample(n=grab_count)

        #save to merchandise table
        df.to_sql('merchandisebuyers', con=engine,
                  if_exists='append', index=False)
        
        # From the dataframe remove 80% of the rows
        df = df.sample(frac=0.2)

        #remove the rows from the session table
        df.to_sql('sessiontable', con=engine,
                  if_exists='replace', index=False)

    
    # Repeat for Mailing list table (1 / 6 of total count)
    with engine.connect() as connection:
        #adjust total count
        result = connection.execute("SELECT COUNT(*) FROM sessiontable;")
        total_count = result.fetchone()[0]

        #adjust grab count
        grab_count = total_count / 6
        
        #save data to pandas dataframe
        df = pd.read_sql_table('sessiontable', engine)
        #grab random rows
        df = df.sample(n=grab_count)

        #save to merchandise table
        df.to_sql('mailinglist', con=engine,
                  if_exists='append', index=False)
        
        # From the dataframe remove 80% of the rows
        df = df.sample(frac=0.2)

        #remove the rows from the session table
        df.to_sql('sessiontable', con=engine,
                  if_exists='replace', index=False)

    # Repeat for regular game attendance table ( 1/ 6 of total count)
    

    # Repeat for parents of KSU students table (1 / 6 of total count)

    # Take the remaining 1/3 of the session table and copy into the alumni table


    # Step 2
    # Any remaining spread evenly across the other tables by random

    # Generate Analysis data from Analytics table
    # Need pie charts of each category, General trends, and a few other things TODO later

    # Data setup step complete
