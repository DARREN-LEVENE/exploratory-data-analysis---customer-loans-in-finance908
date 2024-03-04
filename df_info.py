

class DataFrameInfo:

    '''
    This class contains methods that will generate a variety of useful information for analysis about a data frame
    '''

    def __init__(self, df):
        '''
        Initialiser method
        '''
        self.df = df
    
    def df_datatype_info(self):
        '''
        Method to summarise the data type of each column and the number of non-nulls in each column
        Returns:
            Prints a summary of the number of non-nulls and data type of each column in the data frame
        '''
        return self.df.info()

    def df_stats_summary(self, column):
        '''
        Method to summarise statistical data (such as count, mean, standard deviation) for a specified numerical column
        Args:
            column: data frame column to be analysed
        Returns:
            Summary of statistical data (such as count, mean, standard deviation) for a specified numerical column
        '''
        return self.df[column].describe()

    def df_unique_values(self, column):
        '''
        Method to summarise the frequency of unique values within a category column
        Args:
            column: data frame column to be analysed
        Returns:
            Summary of the frequency of unique values within a categorical column
        '''
        return self.df[column].value_counts()

    def df_shape(self):
        '''
        Method to summarise the total number of rows and columns in the Data Frame
        Returns:
            Prints summary of number of rows and columns in data frame
        '''
        shape = self.df.shape
        return print(f"This dataset has {shape[0]} rows and {shape[1]} columns")

    def df_percent_null(self):
        '''
        Method to calculate the percentage of null values for each column in the data frame
        Returns:
            Prints summary of the pecentage of null values for each column of the data frame   
        '''
        percent_null_vals = (self.df.isnull().sum()*100 / len(self.df)).round(2)
        return percent_null_vals



