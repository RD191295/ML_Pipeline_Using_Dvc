import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import yaml


def load_data(file_name: str) -> pd.DataFrame:
    """
        this function Load Data to pandas DataFrame

        input : 
            file_name (str) : File Name (csv)
        
        output:
            DataFrame (Pandas DataFrame): Pandas DataFrame
    """
    try:
        df = pd.read_csv(file_name)
        return df
    except pd.errors.ParserError as e:
        print(f'Error: Failed to parse the csv file from file {file_name}')
        print(e)
        raise
    except Exception as e:
        print(f'Error: An unexpected error occure while loading data:')
        print(e)
        raise


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
        this function  do pre-processing with dataframe

        input : 
            df (DataFrame) : File Name (csv)
        
        output:
            DataFrame (Pandas DataFrame): Pandas DataFrame
    """
    try:
        df.drop(columns=['tweet_id'],inplace=True)
        final_df = df[df['sentiment'].isin(['happiness','sadness'])]
        final_df['sentiment'].replace({'happiness':1, 'sadness':0},inplace=True)
        return final_df
    except KeyError as e:
        print(f'Error: missing column {e} in the dataframe.')
        print(e)
        raise
    except Exception as e:
        print(f'Error: An unexpected error occure while loading data:')
        print(e)
        raise

def save_data(train_data:pd.DataFrame, test_data:pd.DataFrame, data_path:str)-> None:
    """
        this function  save data in directory

        input : 
            train_data (DataFrame) : train dataset
            test_data (DataFrame) : test dataset
            data_path(str) : directory location where to store data

    """
    try :
        data_path = os.path.join(data_path,'rw')
        os.makedirs(data_path, exist_ok= True)
        train_data.to_csv(os.path.join(data_path,"train.csv"),index=False)
        test_data.to_csv(os.path.join(data_path,"test.csv"),index=False)
    except Exception as e:
        print(f'Error: An unexpected error occure while loading data:')
        print(e)
        raise


def main():
    try:
        df = load_data("D:/Data_Science_Study/Course_Pracitse_Code/MLOPS/ML_Pipeline_Using_Dvc/Dataset/tweet_emotions.csv")
        preprocess_df = preprocess_data(df)
        train_data,test_data = train_test_split(preprocess_df,test_size=0.2,random_state=42)
        save_data(train_data,test_data,data_path= 'D:/Data_Science_Study/Course_Pracitse_Code/MLOPS/ML_Pipeline_Using_Dvc/Dataset') 
    except Exception as e:
        print('Error : {e}')
        print('failed to complete the data ingestion process')


if __name__ == '__main__':
    main()