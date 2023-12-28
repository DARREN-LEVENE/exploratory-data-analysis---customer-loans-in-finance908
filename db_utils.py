import yaml
import psycopg2
from sqlalchemy import create_engine
import pandas as pd

#class definition
class RDSDatabaseConnector:
#class constructor
    '''
    This class contains the methods that will be used to extract data from the RDS database.
    '''
    def __init__(self, credentials):
        '''
        Initialiser method which will take in a dictionary of credentials as the parameter
        Attribute:
            self.the_loaded_file: the loaded the yaml file with credentials
        '''
         
        self.the_loaded_file = self.read_yaml_data(credentials)

    def read_yaml_data(self, filename):
        '''
        This method loads the yaml file containing credentials 
        Args: 
            filename: name of credentials yaml file to be read
        Returns:
            output: credentials dictionary
        '''
        with open(f'{filename}.yaml','r') as f:
            output = yaml.safe_load(f)
            print(output)
            return output

    def init_db_engine(self):
        '''
        This method initialises an SQLalchemy engine from the credentials provided to the class. 
        Returns:
            initialsed engine to connect to database
        '''

        engine_credentials_string = (f"{self.the_loaded_file['RDS_DATABASE_TYPE']}+{self.the_loaded_file['RDS_DBAPI']}://{self.the_loaded_file['RDS_USER']}:{self.the_loaded_file['RDS_PASSWORD']}@{self.the_loaded_file['RDS_HOST']}:{self.the_loaded_file['RDS_PORT']}/{self.the_loaded_file['RDS_DATABASE']}")
        engine = create_engine(engine_credentials_string)
        engine.connect()
        return engine

    def RDS_db_data_extract(self, engine, table_name):
        '''
        This method extracts data from the RDS database and returns it as a pandas dataframe
        Args:
            engine: engine to connect to database
            table_name: name of table to be read
        Returns:
            df: Dataframe extracted from the Database
        '''

        with engine.connect() as conn:
            df = pd.read_sql_table(table_name, conn)
        df.head()
        return df

    def save_df_to_csv(self, df, csv_filename, output_directory):
        '''
        This method saves the data to an csv file at specified location on computer
        Args:
            df: dataframe to be saved as csv
            csv_filename: csv file name 
            output_directory: filepath location of where to save csv file
        '''

        #construct the full filepath
        csv_path = f"{output_directory}/{csv_filename}"
        #save DataFrame to csv file
        df.to_csv(csv_path, index = False)
        print(f"DataFrame saved to {csv_path}")


connector = RDSDatabaseConnector("credentials")
engine = connector.init_db_engine()
df = connector.RDS_db_data_extract(engine, "loan_payments")
filename = "loan_payments.csv"
output_directory = "E:\WilmingtonConsultingLimitedyeJan2015\AICore\exploratory-data-analysis---customer-loans-in-finance908"
connector.save_df_to_csv(df, filename, output_directory)
