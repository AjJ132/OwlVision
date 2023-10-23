import sqlalchemy as db
import pandas as pd
import random
from faker import Faker
from datetime import date, timedelta

fake = Faker()

def perform_operations(engine):
    # Initialize DataFrames
    session_df = pd.read_sql_table('sessiontable', engine)
    
    # Common steps to get grab_count and total_count
    total_count = len(session_df)
    print(f"Total count of rows: {total_count}")
    grab_count = int(total_count / 2)

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

    
    indices_to_remove = merchandise_df.sample(frac=0.8, replace=True).index
    session_df = session_df.drop(indices_to_remove)
    print(f"Removed {len(indices_to_remove)} rows for merchandise.")

    #------------------------------------------------------------------------------------------------------------

    # Operations for Mailing List
    grab_count = 0
    total_count = len(session_df)
    grab_count = int(total_count / 4)

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
    grab_count = int(total_count / 3)


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
    indices_to_remove = alumni_df.sample(frac=0.8, replace=True).index
    session_df = session_df.drop(indices_to_remove)
    print(f"Removed {len(indices_to_remove)} rows for alumni.")

    # ------------------------------------------------------------------------------------------------------------

    #Operations for Previous Ticket Buyers
    total_count = len(session_df)
    grab_count = int(total_count / 2)

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

    #create new df for multiple ticket purchases
    multiple_ticket_purchases_df = pd.DataFrame(columns=['id', 'first_name', 'last_name', 'purchasedate', 'moneyspent', 'gamedate'])

    #set values for previous ticket buyers
    for index, row in previous_ticket_buyers_df.iterrows():
        #potential game dates
        potential_dates = [
            date(2023, 8, 31),
            date(2023, 9, 16),
            date(2023, 10, 7),
            date(2023, 10, 28),
            date(2019, 8, 31),
            date(2019, 9, 21),
            date(2019, 10, 12),
            date(2019, 10, 19),
            date(2019, 11, 9),
            date(2019, 11, 30),
            date(2020, 10, 10),
            date(2020, 10, 24),
            date(2020, 11, 14),
            date(2021, 9, 2),
            date(2021, 10, 2),
            date(2021, 10, 16),
            date(2021, 10, 30),
            date(2022, 9, 24),
            date(2022, 10, 8),
            date(2022, 10, 15),
            date(2022, 10, 22),
            date(2022, 10, 29),
            date(2022, 11, 12)
            ]

        #randomly select a date from potential dates
        gamedate = random.choice(potential_dates)
        
        #randomly select a purchase date that is within 100 days of the game date
        delta = timedelta(days=random.randint(0, 100))  # Generating a random timedelta between 0 and 100 days
        purchasedate = gamedate - delta  # Subtracting the timedelta from gamedate to get purchase date
        
        #randomly select a money spent value
        moneyspent = random.randint(30, 120)

        # Update the DataFrame
        previous_ticket_buyers_df.at[index, 'purchasedate'] = purchasedate
        previous_ticket_buyers_df.at[index, 'moneyspent'] = moneyspent
        previous_ticket_buyers_df.at[index, 'gamedate'] = gamedate

    
        #a 1/4 chance of them getting another ticket purchase
        while random.randint(0, 3) == 0:
            #grab first and last name and repeat the process
            id = row['id']
            first_name = row['first_name']
            last_name = row['last_name']

            #grab random date from potential dates
            gamedate = random.choice(potential_dates)

            #randomly select a purchase date that is within 100 days of the game date
            delta = timedelta(days=random.randint(0, 100))  # Generating a random timedelta between 0 and 100 days

            # Subtracting the timedelta from gamedate to get purchase date
            purchasedate = gamedate - delta

            #randomly select a money spent value
            moneyspent = random.randint(30, 150)

            #create a new row with the same first and last name
            new_row = {'id': id, 'first_name': first_name, 'last_name': last_name, 'purchasedate': purchasedate, 'moneyspent': moneyspent, 'gamedate': gamedate}

            #add row to new dataframe
            multiple_ticket_purchases_df = multiple_ticket_purchases_df.append(new_row, ignore_index=True)

            print("Added another ticket purchase for " + first_name + " " + last_name + ".")

    #remove rows from session_df
    indices_to_remove = previous_ticket_buyers_df.sample(frac=0.8, replace=True).index

    #remove rows from session_df and ignore errors as they are from the person buying multiple tickets
    session_df = session_df.drop(indices_to_remove, errors='ignore')

    #add rows from multiple ticket purchases to previous ticket buyers
    previous_ticket_buyers_df = previous_ticket_buyers_df.append(multiple_ticket_purchases_df, ignore_index=True)


    print(f"Removed {len(indices_to_remove)} rows for previous ticket buyers.")

    # ------------------------------------------------------------------------------------------------------------

    #Operations to spread the remaining rows across all tables at random
    
    print("Starting to spread remaining rows across all tables...")

    #While there are still rows in session_df, randomly select a row and add it to a random table
    for index, row in session_df.iterrows():
        cloned_row = row.to_dict()

        #randomly select a table to add the row to
        table = random.choice(["merchandisebuyers", "mailinglist", "alumni", "regularticketbuyers"])
        # table = random.choice(["merchandisebuyers", "mailinglist"])

        #TEMP
        # table = "alumni"

        try:
            #case switch for table
            if table == "merchandisebuyers":
                #Generate fields and remove home address column
                
                del cloned_row['home_address']
                
                #add purchasedate and moneyspent columns
                cloned_row['purchasedate'] = ''
                cloned_row['moneyspent'] = ''

                #generate random date and money spent
                random_date = fake.date_between(start_date='-5y', end_date='today')
                
                # Convert the date object to a string in 'YYYY-MM-DD' format
                date_str = random_date.strftime('%Y-%m-%d')
                
                # # Update the DataFrame
                cloned_row['purchasedate'] = date_str
                cloned_row['moneyspent'] = random.randint(0, 150)

                #add row to merchandise buyers
                merchandise_df = merchandise_df.append(pd.DataFrame([cloned_row]), ignore_index=True)

                

            elif table == "mailinglist":
                #remove home address column
                del cloned_row['home_address']

                #add row to mailing list
                mailing_list_df = mailing_list_df.append(pd.DataFrame([cloned_row]), ignore_index=True)
                
            elif table == "alumni":
                cloned_row['gender'] = ''
                cloned_row['age'] = ''
                cloned_row['streetaddress'] = ''
                cloned_row['city'] = ''
                cloned_row['usstate'] = ''
                cloned_row['zipcode'] = ''
                cloned_row['dateenrolled'] = ''
                cloned_row['gradyear'] = ''
                cloned_row['degree'] = ''
                cloned_row['major'] = ''
                cloned_row['stillattending'] = ''

                #Random chance for gender
                gender = "male" if random.randint(0, 1) == 0 else "female"

                #Random chance for age (23 - 40)
                age = random.randint(23, 40)

                #parse via ',' address to get street address, city, state, and zip code
                address = cloned_row['home_address']
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
                cloned_row['gender'] = gender
                cloned_row['age'] = age
                cloned_row['streetaddress'] = streetAddress
                cloned_row['city'] = city
                cloned_row['usstate'] = usstate
                cloned_row['zipcode'] = zipcode
                cloned_row['dateenrolled'] = dateenrolled
                cloned_row['gradyear'] = gradyear
                cloned_row['degree'] = degree
                cloned_row['major'] = major
                cloned_row['stillattending'] = stillattending


                #remove address column
                del cloned_row['home_address']

                #add row to alumni
                print("Adding row to alumni...")
                alumni_df = alumni_df.append(pd.DataFrame([cloned_row]), ignore_index=True)

            elif table == "regularticketbuyers":
                #add columns for previous ticket buyers
                cloned_row['purchasedate'] = ''
                cloned_row['moneyspent'] = ''
                cloned_row['gamedate'] = ''

                #remove address, phone number, and email columns
                del cloned_row['home_address']
                del cloned_row['phone_number']
                del cloned_row['email']


                #set values for previous ticket buyers
                #potential game dates
                potential_dates = [
                    date(2023, 8, 31),
                    date(2023, 9, 16),
                    date(2023, 10, 7),
                    date(2023, 10, 28),
                    date(2019, 8, 31),
                    date(2019, 9, 21),
                    date(2019, 10, 12),
                    date(2019, 10, 19),
                    date(2019, 11, 9),
                    date(2019, 11, 30),
                    date(2020, 10, 10),
                    date(2020, 10, 24),
                    date(2020, 11, 14),
                    date(2021, 9, 2),
                    date(2021, 10, 2),
                    date(2021, 10, 16),
                    date(2021, 10, 30),
                    date(2022, 9, 24),
                    date(2022, 10, 8),
                    date(2022, 10, 15),
                    date(2022, 10, 22),
                    date(2022, 10, 29),
                    date(2022, 11, 12)
                    ]

                #randomly select a date from potential dates
                gamedate = random.choice(potential_dates)
                
                #randomly select a purchase date that is within 100 days of the game date
                delta = timedelta(days=random.randint(0, 100))  # Generating a random timedelta between 0 and 100 days
                purchasedate = gamedate - delta  # Subtracting the timedelta from gamedate to get purchase date
                
                #randomly select a money spent value
                moneyspent = random.randint(30, 150)
                
                # Update the DataFrame
                cloned_row['purchasedate'] = purchasedate
                cloned_row['moneyspent'] = moneyspent
                cloned_row['gamedate'] = gamedate

                #add row to regular ticket buyers
                print("Adding row to regular ticket buyers...")
                previous_ticket_buyers_df = previous_ticket_buyers_df.append(pd.DataFrame([cloned_row]), ignore_index=True)
                    
            else:
                print("Error: table not found")

            #remove row from session_df
            print("Removing row from session_df...")
            session_df.drop(index, inplace=True)

        except Exception as e:
            print(f"An error occurred: {e}")
            print(f"Row: {cloned_row}")
            print(f"Table: {table}")

    
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
            #DEBUG: print count of merchandise_df
            print(f"Count of merchandise_df: {len(merchandise_df)}")
            print("Updating merchandise buyers...")
            merchandise_df.to_sql('merchandisebuyers', con=engine, if_exists='replace', index=False)

            #DEBUG: print count of mailing_list_df
            print(f"Count of mailing_list_df: {len(mailing_list_df)}")
            print("Updating mailing list...")
            mailing_list_df.to_sql('mailinglist', con=engine, if_exists='replace', index=False)

            #DEBUG: print count of alumni_df
            print(f"Count of alumni_df: {len(alumni_df)}")
            print("Updating alumni...")
            alumni_df.to_sql('alumni', con=engine, if_exists='replace', index=False)

            #DEBUG: print count of regularticketbuyers_df
            print(f"Count of regularticketbuyers_df: {len(regularticketbuyers_df)}")
            print("Updating regular ticket buyers...")
            regularticketbuyers_df.to_sql('regularticketbuyers', con=engine, if_exists='replace', index=False)

            print("Updating session table...")
            #DEBUG: print count of session_df
            print(f"Count of session_df: {len(session_df)}")

            session_df.to_sql('sessiontable', con=engine, if_exists='replace', index=False)
            
            trans.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            trans.rollback()

# initial_data_setup()
