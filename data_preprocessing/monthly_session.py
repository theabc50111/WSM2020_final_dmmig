import sys
import os
import pandas as pd
import numpy as np

def month_sess(sess_path,out_path):
    '''
    sess_path: csv file for sessions
    out_path: folder to save sessions by month
    '''
    ses_df = pd.read_csv(sess_path)
    #dealing datetime format
    ses_df.date = ses_df.date.apply(lambda x:x.split(".")[0] if "." in x else x)
    ses_df["datetime"] = pd.to_datetime(ses_df.date,format="%Y-%m-%d %H:%M:%S")
    #print(ses_df.datetime.dt.year.unique())
    #print(ses_df.datetime.dt.month.unique()) 
    # loop thru year save per month
    for year in ses_df.datetime.dt.year.unique():
        print("dealing with year: {} data".format(year))
        year_ses = ses_df[ses_df.datetime.dt.year==year]
        for month in year_ses.datetime.dt.month.unique():
            print("dealing with month: {} data".format(month))
            month_ses = year_ses[year_ses.datetime.dt.month==month]
            month_ses.to_csv(out_path+str(year)+"_"+str(month)+"session.csv",index=False)
    #print(ses_df.datetime.unique())
    return


if __name__=="__main__":
    month_sess("../../recsys2022/train_purchases.csv","../datasets/monthly_cand/")
