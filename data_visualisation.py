import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from statsmodels.graphics.gofplots import qqplot
from matplotlib import pyplot


class Plotter:
    '''
    This class contains methods that will visualise insights from the data in graphical form
    '''
    def __init__ (self, df):

        self.df = df

        
    def histogram_plot (self, column, df):

        df[column].hist(bins=50)
        return plt.show()
    
    
    def kernel_density_estimate_plot (self, column, df):

        sns.histplot(data = df, x = column, kde = True)
        return sns.despine()
    
    
    def box_and_whiskers_plot (self, column, df):

        box_plot = px.box(df, y = column, width = 600, height = 500)
        return box_plot.show()


    def violin_plot (self, column, df):

        sns.violinplot(data = df, y = column)
        return sns.despine()
    
    @staticmethod
    def correlation_heatmap (df):
        df = df.select_dtypes(include = "number")
        selected_corr = df.corr()
        return sns.heatmap(selected_corr, annot = True, cmap = "coolwarm")
    

    def qq_plotter (self, column, df):

        qq_plot = qqplot(df[column], scale = 1, line = "q", fit = True)
        return pyplot.show()