import missingno as msno
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
from scipy.stats import yeojohnson
from sklearn.preprocessing import PowerTransformer

class DataFrameTransform:

    def __init__(self,df):
        self.df = df
    
    def drop_rows(self, column):
        self.df.dropna(subset = [column], axis = 0, inplace = True)
        return self.df

    def drop_columns(self, column):
        self.df.drop(column, axis = 1, inplace = True)
        return self.df

    
    def imputed_median(self, column):
        self.df[column].fillna(self.df[column].median(), inplace = True)
        return self.df


    def imputed_mean(self, column):
        self.df[column].fillna(self.df[column].mean(), inplace = True)
        return self.df
    

    def imputed_mode(self, column):
        self.df[column].fillna(self.df[column].mode(), inplace = True)
        return self.df


    def missingno_plot(self, df):
        return msno.matrix(df)
    

    def log_transform(self, column):
        log_column = self.df[column].map(lambda i: np.log(i) if i > 0 else 0)
        return log_column.skew()
    

    def box_cox_transform(self, column):
        boxcox_transform = self.df[column]
        boxcox_transform = stats.boxcox(boxcox_transform)
        boxcox_transform = pd.Series(boxcox_transform[0])
        return boxcox_transform.skew()


    def yeo_johnson_transform(self, column):
        yeojohnson_transform = self.df[column]
        yeojohnson_transform = stats.yeojohnson(yeojohnson_transform)
        yeojohnson_transform = pd.Series(yeojohnson_transform[0])
        return yeojohnson_transform.skew()
    
    
    def yeo_johnson_transform_df(self, column):
        column_data = self.df[column].values.reshape(-1, 1)

        power_transformer = PowerTransformer(method="yeo-johnson", standardize = True)
        self.df[column] = power_transformer.fit_transform(column_data)

        print(f"Transformed column '{column}':\n{self.df[column]}")
        return self.df
    

    def box_cox_transform_df(self, column):
        column_data = self.df[column].values.reshape(-1, 1)

        power_transformer = PowerTransformer(method="box-cox", standardize = True)
        self.df[column] = power_transformer.fit_transform(column_data)

        print(f"Transformed column '{column}':\n{self.df[column]}")
        return self.df
    
    
    def log_transform_df(self, column):        
        self.df[column] = self.df[column].map(lambda i: np.log(i) if i > 0 else 0)
        return self.df
    
    def z_scores(self, column, threshold = 3):
        mean_column = np.mean(self.df[column])
        std_column = np.std(self.df[column])
        z_scores = np.abs((self.df[column] - mean_column) / std_column)
        self.df.loc[z_scores > threshold, column] = mean_column
            