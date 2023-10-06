import sqlalchemy as db
import pandas as pd
import random
from faker import Faker
from datetime import datetime

fake = Faker()

def perform_operations(engine):
    # Initialize DataFrames
    session_df = pd.read_sql_table('sessiontable', engine)
    
    # Common steps to get grab_count and total_count
    total_count = len(session_df)
    print(f"Total count of rows: {total_count}")
    grab_count = int(total_count / 4)

    # add randomness to grab_count
    grab_count += random.randint(-200, 200)
    
    # Operations for Merchandise Buyers
    merchandise_df = session_df.sample(n=grab_count)
    merchandise_df = merchandise_df.drop(columns=['home_address'])

    for index, row in merchandise_df.iterrows():
        random_date = fake.date_between(start_date='-5y', end_date='today')

        # Convert the date object to a string in 'YYYY-MM-DD' format
        date_str = random_date.strftime('%Y-%m-%d')
        
        # Update the DataFrame
        merchandise_df.at[index, 'purchasedate'] = date_str
        merchandise_df.at[index, 'moneyspent'] = random.randint(0, 150)

    
    indices_to_remove = merchandise_df.sample(frac=0.2, replace=True).index
    session_df = session_df.drop(indices_to_remove)
    print(f"Removed {len(indices_to_remove)} rows for merchandise.")

    #------------------------------------------------------------------------------------------------------------

    # Operations for Mailing List
    grab_count = 0
    total_count = len(session_df)
    grab_count = int(total_count / 5)

    # add randomness to grab_count
    grab_count += random.randint(-200, 200)

    mailing_list_df = session_df.sample(n=grab_count)
    mailing_list_df = mailing_list_df.drop(columns=['home_address'])
    indices_to_remove = mailing_list_df.sample(frac=0.8).index
    session_df = session_df.drop(indices_to_remove)
    print(f"Removed {len(indices_to_remove)} rows for mailing list.")

    #------------------------------------------------------------------------------------------------------------

    # Operations for Alumni
    total_count = len(session_df)
    grab_count = int(total_count / 4)


    # add randomness to grab_count
    grab_count += random.randint(-200, 200)

    #ensure grab_count is not greater than total_count
    if grab_count > total_count:
        print("Grab count is greater than total count. Setting to total count.")
        grab_count = total_count - 200

    #ensure grab_count is not less than 0
    if grab_count < 0:
        grab_count = 0
        print("Grab count is less than 0. Setting to 0.")
    
    
    alumni_df = session_df.sample(n=grab_count)

    #Add columns for alumni (Gender, age, streetAddress, city, usstate, zipcode, dateenrolledm gradyear, degree, major, stillattending)
    alumni_df['gender'] = ''
    alumni_df['age'] = ''
    alumni_df['streetaddress'] = ''
    alumni_df['city'] = ''
    alumni_df['usstate'] = ''
    alumni_df['zipcode'] = ''
    alumni_df['dateenrolled'] = ''
    alumni_df['gradyear'] = ''
    alumni_df['degree'] = ''
    alumni_df['major'] = ''
    alumni_df['stillattending'] = ''

    #set all values for alumni
    for index, row in alumni_df.iterrows():
        #Random chance for gender
        gender = "male" if random.randint(0, 1) == 0 else "female"

        #Random chance for age (23 - 40)
        age = random.randint(23, 40)

        #parse via ',' address to get street address, city, state, and zip code
        address = row['home_address']
        try:
            # Split the address by ','
            address_parts = address.split(',')
            
            # Assign to variables
            streetAddress = address_parts[0].strip()
            city = address_parts[1].strip()
            
            # For US state, grab the first two characters of the state
            usstate = address_parts[2].strip()[:2]
            
            # For zip code, grab the remainder
            zipcode = address_parts[2].strip()[3:]

            #TEMP ERROR HANDLING/CORRECTION
            #ONLY GRAB THE LAST 5 CHARACTERS FOR ZIP CODE
            zipcode = zipcode[-5:]
            
        except Exception as e:
            #grab last 5 for zip code
            zipcode = address[-5:]

            #Set default value to state and city
            usstate = "--"
            city = "--"
           

        # Set date enrolled to be iwthin the last 10 and 5 years
        dateenrolled = fake.date_between(start_date='-10y', end_date='-5y')

        #set grad year to be 4-5 years after date enrolled
        gradyear = dateenrolled.year + random.randint(4, 5)

        #set degree to be random
        degree = random.choice(["Bachelor's", "Master's"])

        #set major to be random
        major = random.choice([
            "Computer Science",
            "Computer Engineering",
            "Information Technology",
            "Information Systems",
            "Software Engineering",
            "Computer Information Systems",
            "Biology",
            "Chemistry",
            "Physics",
            "Mathematics",
            "English Literature",
            "History",
            "Philosophy",
            "Psychology",
            "Sociology",
            "Political Science",
            "Economics",
            "Business Administration",
            "Marketing",
            "Finance",
            "Accounting",
            "Graphic Design",
            "Fine Arts",
            "Music",
            "Theatre Arts",
            "Journalism",
            "Communication Studies",
            "Environmental Science",
            "Astronomy",
            "Geography",
            "Anthropology",
            "Education"
        ])

        #set still attending to be a 5% chance of being true
        stillattending = "true" if random.randint(0, 100) < 5 else "false"

        # Update the DataFrame
        alumni_df.at[index, 'gender'] = gender
        alumni_df.at[index, 'age'] = age
        alumni_df.at[index, 'streetaddress'] = streetAddress
        alumni_df.at[index, 'city'] = city
        alumni_df.at[index, 'usstate'] = usstate
        alumni_df.at[index, 'zipcode'] = zipcode
        alumni_df.at[index, 'dateenrolled'] = dateenrolled
        alumni_df.at[index, 'gradyear'] = gradyear
        alumni_df.at[index, 'degree'] = degree
        alumni_df.at[index, 'major'] = major
        alumni_df.at[index, 'stillattending'] = stillattending


    #remove address column
    alumni_df = alumni_df.drop(columns=['home_address'])

    indices_to_remove = []
    indices_to_remove = alumni_df.sample(frac=0.2, replace=True).index
    session_df = session_df.drop(indices_to_remove)
    print(f"Removed {len(indices_to_remove)} rows for alumni.")

    # ------------------------------------------------------------------------------------------------------------

    #Operations for Previous Ticket Buyers
    total_count = len(session_df)
    grab_count = int(total_count / 4)

    # add randomness to grab_count
    grab_count += random.randint(-200, 200)

    #ensure grab_count is not greater than total_count
    if grab_count > total_count:
        print("Grab count is greater than total count. Setting to total count.")
        grab_count = total_count - 200

    #ensure grab_count is not less than 0
    if grab_count < 0:
        grab_count = 0
        print("Grab count is less than 0. Setting to 0.")

    #grab random rows from session_df
    previous_ticket_buyers_df = session_df.sample(n=grab_count)

    #Remove address, phone number, and email columns
    previous_ticket_buyers_df = previous_ticket_buyers_df.drop(columns=['home_address', 'phone_number', 'email'])

    #add columns for previous ticket buyers
    previous_ticket_buyers_df['purchasedate'] = ''
    previous_ticket_buyers_df['moneyspent'] = ''
    previous_ticket_buyers_df['gamedate'] = ''

    #set values for previous ticket buyers
    for index, row in previous_ticket_buyers_df.iterrows():
        #potential game dates
        potential_dates = [
            "Aug 31, 2023",
            "Sep 16, 2023",
            "Oct 7, 2023",
            "Oct 28, 2023",
            "Aug 31, 2019",
            "Sep 21, 2019",
            "Oct 12, 2019",
            "Oct 19, 2019",
            "Nov 9, 2019",
            "Nov 30, 2019",
            "Oct 10, 2020",
            "Oct 24, 2020",
            "Nov 14, 2020",
            "Sep 2, 2021",
            "Oct 2, 2021",
            "Oct 16, 2021",
            "Oct 30, 2021",
            "Sep 24, 2022",
            "Oct 8, 2022",
            "Oct 15, 2022",
            "Oct 22, 2022",
            "Oct 29, 2022",
            "Nov 12, 2022"
        ]

        formatted_dates = [datetime.strptime(date, "%b %d, %Y").date() for date in potential_dates]


        #randomly select a date from potential dates
        gamedate = random.choice(formatted_dates)

        #randomly select a purchase date that is within 100 days of the game date
        purchasedate = fake.date_between(start_date='-100d', end_date=gamedate)

        #randomly select a money spent value
        moneyspent = random.randint(30, 150)

        # Update the DataFrame
        previous_ticket_buyers_df.at[index, 'purchasedate'] = purchasedate
        previous_ticket_buyers_df.at[index, 'moneyspent'] = moneyspent
        previous_ticket_buyers_df.at[index, 'gamedate'] = gamedate

    
    indices_to_remove = previous_ticket_buyers_df.sample(frac=0.2, replace=True).index
    session_df = session_df.drop(indices_to_remove)

    print(f"Removed {len(indices_to_remove)} rows for previous ticket buyers.")

    # ------------------------------------------------------------------------------------------------------------


    return session_df, merchandise_df, mailing_list_df, alumni_df, previous_ticket_buyers_df

def initial_data_setup():
    engine = db.create_engine('postgresql+psycopg2://admin:password@localhost:5432/OwlVisionPrototype')

    with engine.connect() as connection:
        connection.execute("DELETE FROM sessiontable;")
        connection.execute("INSERT INTO sessiontable SELECT * FROM generaluserpool;")
        connection.execute("DELETE FROM merchandisebuyers;")
        connection.execute("DELETE FROM mailinglist;")
        connection.execute("DELETE FROM alumni;")
        connection.execute("DELETE FROM regularticketbuyers;")
        
    session_df, merchandise_df, mailing_list_df, alumni_df, regularticketbuyers_df = perform_operations(engine)

    with engine.connect() as connection:
        trans = connection.begin()
        try:
            print("Updating database tables...")
            # Update Database Tables
            print("Updating merchandise buyers...")
            merchandise_df.to_sql('merchandisebuyers', con=engine, if_exists='replace', index=False)

            print("Updating mailing list...")
            mailing_list_df.to_sql('mailinglist', con=engine, if_exists='replace', index=False)

            print("Updating alumni...")
            alumni_df.to_sql('alumni', con=engine, if_exists='replace', index=False)

            print("Updating regular ticket buyers...")
            regularticketbuyers_df.to_sql('regularticketbuyers', con=engine, if_exists='replace', index=False)

            print("Updating session table...")
            session_df.to_sql('sessiontable', con=engine, if_exists='replace', index=False)
            
            trans.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            trans.rollback()

def convert_to_date(date_str):
    return datetime.strptime(date_str, "%b %d, %Y").date()

initial_data_setup()
