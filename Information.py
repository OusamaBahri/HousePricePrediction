import pandas as pd
class Information:
    """This class shows some information about 
    the dataset
    """
    def __init__(self):
        print("\n Information object is created \n")
        
    def get_missing_values(self, data):
        """this function finds the missing values
        in the dataset

        Args:
            data (Pandas Dataframe): The data you want to see information about
            
        Returns:
            A Pandas Series contains the missing values in descending order
        """
                #get the sum of all missing values in the dataset
        missing_values = data.isnull().sum()
        #sorting the missing values in a pandas Series
        missing_values = missing_values.sort_values(ascending=False)
        
        #returning the missing values Series
        return missing_values
