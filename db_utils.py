import yaml
import psycopg2
from sqlalchemy import create_engine
import pandas as pd

#class definition
class RDSDatabaseConnector:
#class constructor
    def __init__(self, credentials):
         
        self.the_loaded_file = self.read_yaml_data(credentials)

    def read_yaml_data(self, filename):

        with open(f'{filename}.yaml','r') as f:
            output = yaml.safe_load(f)
            print(output)
            return output

    def init_db_engine(self):

        engine_credentials_string = (f"{self.the_loaded_file['RDS_DATABASE_TYPE']}+{self.the_loaded_file['RDS_DBAPI']}://{self.the_loaded_file['RDS_USER']}:{self.the_loaded_file['RDS_PASSWORD']}@{self.the_loaded_file['RDS_HOST']}:{self.the_loaded_file['RDS_PORT']}/{self.the_loaded_file['RDS_DATABASE']}")
        engine = create_engine(engine_credentials_string)
        engine.connect()
        return engine

    def RDS_db_data_extract(self, engine, table_name):

        with engine.connect() as conn:
            loan_payments = pd.read_sql_table(table_name, conn)
        loan_payments.head()
        return loan_payments

    def save_df_to_csv(self, loan_payments, csv_filename, output_directory):

        #construct the full filepath
        csv_path = f"{output_directory}/{csv_filename}"
        #save DataFrame to csv file
        loan_payments.to_csv(csv_path, index = False)
        print(f"DataFrame saved to {csv_path}")


connector = RDSDatabaseConnector("credentials")
engine = connector.init_db_engine()
df = connector.RDS_db_data_extract(engine, "loan_payments")
filename = "loan_payments.csv"
output_directory = "E:\WilmingtonConsultingLimitedyeJan2015\AICore\exploratory-data-analysis---customer-loans-in-finance908"
connector.save_df_to_csv(df, filename, output_directory)
