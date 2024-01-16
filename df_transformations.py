import pandas as pd

class DataTransform:

    '''
    This class contains methods that will transform data frame columns into the correct format and data type

    '''

    def __init__(self,df):
        '''
        Initialiser method
        '''
        self.df = df
    
    def convert_to_datetime(self, column):
        '''
        This method converts data frame column to datetime datatype
        Args:
            column: data frame column to be transformed
        '''
        self.df[column] = pd.to_datetime(self.df[column])
        

    def cast_to_category(self, column): 
        '''
        This method casts data frame column to category data type
        Args:
            column: data frame column to be transformed
        '''
        self.df[column] = self.df[column].astype("category")

    
    def convert_to_categorical(self, column):
        '''
        This method assigns a numerical value to ordinal categorical variables
        Args:
            column: data frame column to be transformed
        '''
        self.df[column] = pd.Categorical(self.df[column], ordered=True).codes
    
   