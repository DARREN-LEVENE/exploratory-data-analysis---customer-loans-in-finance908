import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from matplotlib import pyplot
from statsmodels.graphics.gofplots import qqplot

class Plotter:
    '''
    This class contains methods that will visualise insights from the data in graphical form
    #TO DO: doc strings
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
        fig, ax = plt.subplots(figsize=(20, 20))
        return sns.heatmap(selected_corr, annot = True, cmap = "coolwarm", ax=ax)
    

    def qq_plotter (self, column, df):

        qq_plot = qqplot(df[column], scale = 1, line = "q", fit = True)
        return pyplot.show()
    