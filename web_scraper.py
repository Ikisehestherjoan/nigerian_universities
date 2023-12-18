# ==============IMPORT ALL NECESSARY LIBRARIES
import pandas as pd
import datetime
import psycopg2
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from configparser import ConfigParser  # Corrected import statement

config = ConfigParser()
config.read('.env')

# Database credentials
db_user = config['DB_CONN']['db_user']
db_password = config['DB_CONN']['pass']  # Corrected variable name
db_host = config['DB_CONN']['db_host']
db_database = config['DB_CONN']['db_database']

#Data Extraction Layer
def extract_data():
    #data = pd.DataFrame()
    url ='https://en.wikipedia.org/wiki/List_of_universities_in_Nigeria'
    scrapped_data =requests.get(url)
    scrapped_data = scrapped_data.content
    soup = BeautifulSoup(scrapped_data,'lxml')
    html_data = str(soup.find_all('table'))
    dfs = pd.read_html(html_data)[0:7]
    uni_data = pd.concat(dfs)
    uni_data.to_csv('raw_universities_in_ngn.csv', index = False)
    print('Data Successfully written to a csv file')



# DATA LOAD TRANSFORMATION LAYER

def transform_data():
    data = pd.read_csv('raw_universities_in_ngn.csv')  # reading data into csv
    filtered_df = data.dropna(thresh=len(data.columns) - 2)
    # Use a lambda function with str.extract to extract the years
    filtered_df[['Founded', 'end_year']] = filtered_df['Founded'].str.extract(r'(\d{4})[^2]*(\d{4})?')
    print(filtered_df)

# # Drop the  'end_year,0,1' column
    filtered_df.drop(['end_year','0','1'], axis=1, inplace=True)
    #print(filtered_df)
    
 
    def get_fees(value):
        if value =='Federal':
            return '120,000'
        elif value =='State':
            return '300,000'
        elif value =='Private':
            return '850,000'
        else:
            return 'NO FEES'
    filtered_df['Fee'] = filtered_df['Funding'].apply(get_fees)
    #print(filtered_df.tail())
   # filtered_df=filtered_df[['Name','State','Abbreviation','Location','Funding','Founded','Fee']]
    filtered_df.to_csv('transformed_data.csv', index=False)
    print('Data transformation and file written to csv')
transform_data()


# # loading to postgresql
# def loading_to_db():
#     data = pd.read_csv('transformed_data.csv')
#     engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}/{db_database}')
#     data.to_sql('ngn_unversity',con=engine, if_exists='append', index=False)
# loading_to_db()
# print('data loaded')


#extract_data()