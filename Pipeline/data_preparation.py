import sqlalchemy as db
import pandas as pd
import random
import os


def prepare_data():
    #First gather the data from the database and save as CSV into folder
    #Then, read the CSV and identify trends
    #lastly, save the trends as a CSV/excel file

    #Connect to the database
    engine = db.create_engine('postgresql+psycopg2://admin:password@localhost:5432/OwlVisionPrototype')

    with engine.connect() as connection:
        #Get the data from the database into a dataframe
        merchandise_buyers_df = pd.read_sql_table('merchandisebuyers', engine)
        mailing_list_df = pd.read_sql_table('mailinglist', engine)
        alumni_df = pd.read_sql_table('alumni', engine)
        regular_ticket_buyers_df = pd.read_sql_table('regularticketbuyers', engine)

        #create init_data folder if it doesn't exist
        folder_name = "init_data"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        #Save the dataframes as CSV files
        merchandise_buyers_df.to_csv('Init_Data/merchandise_buyers.csv')
        mailing_list_df.to_csv('Init_Data/mailing_list.csv')
        alumni_df.to_csv('Init_Data/alumni.csv')
        regular_ticket_buyers_df.to_csv('Init_Data/regular_ticket_buyers.csv')

        #First trend, search across all tables for people with same first and last name
        #if that person shares an email address or phone number, then they are the same person
        #if that person is fond across more than three tables, then they are a super user
        #create new df with regular users and super users
        #mark super users with how many tables they are found in
        #save the new df as a CSV file

        #add email and phone number columns to the alumni and regular ticket buyers df since it is not in the database
        regular_ticket_buyers_df = regular_ticket_buyers_df.assign(
            email="N/A",
            phone_number="N/A"
        )

        common_cols = ['first_name', 'last_name', 'email', 'phone_number']
        all_data_df = pd.concat([
            merchandise_buyers_df[common_cols].assign(source='merchandise_buyers'),
            mailing_list_df[common_cols].assign(source='mailing_list'),
            alumni_df[common_cols].assign(source='alumni'),
            regular_ticket_buyers_df[common_cols].assign(source='regular_ticket_buyers')
        ], ignore_index=True)

        print("merged")

        #add user_type column to the dataframe
        all_data_df['user_type'] = 'regular_user'
    
        # Categorize users
        all_data_df['user_type'] = all_data_df.groupby(['first_name', 'last_name'])['source'].transform(categorize_and_print_users)

        # Save the new dataframe as a CSV file
        all_data_df.to_csv('Init_Data/all_data.csv')
        
        #Create a new dataframe with only the super users
        super_users_df = all_data_df[all_data_df['user_type'] == 'super_user']

        #Save the super users dataframe as a CSV file
        super_users_df.to_csv('Init_Data/super_users.csv')

        #create a new dataframe with only the semi super users
        semi_super_users_df = all_data_df[all_data_df['user_type'] == 'semi_super_user']

        #save the semi super users dataframe as a CSV file
        semi_super_users_df.to_csv('Init_Data/semi_super_users.csv')

        #Create a new dataframe with only the regular users
        regular_users_df = all_data_df[all_data_df['user_type'] == 'regular_user']

        #Save the regular users dataframe as a CSV file
        regular_users_df.to_csv('Init_Data/regular_users.csv')


def categorize_and_print_users(x):
    if x.nunique() >= 3:
        print(f"Super user detected: {x.name}")  # x.name contains the group labels, in this case, (first_name, last_name)
        return 'super_user'
    # elif x.unique() == 1:
    #     return 'semi_super_user'
    else:
        return 'regular_user'
        

prepare_data()



    

