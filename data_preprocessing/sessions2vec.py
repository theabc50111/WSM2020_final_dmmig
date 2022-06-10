import pandas as pd
import time
import sys
import numpy as np
sys.argv
def items2vec(_df_item,_session_items):
    session_vec = np.sum(_df_item.loc[pd.Index(_session_items)]).values
    return session_vec 

def sessions2vec(item_path,session_path):
    '''
    input 1 dataframe with col name :session_id,item_id
    input 2 path of session.csv
    '''
    #item_vec裡面需要有col:session_id,item_id
    s_t = time.time()
    _df_session = pd.read_csv(session_path)
    _df_item = pd.read_csv(item_path,index_col=0).set_index("item_id")
    pre_sid = None
    session_dic={}
    item_buf=[]
    for row in _df_session.iterrows():#tuple of row value,row[0]=index,row[1]=values
        if pre_sid!=row[1].session_id:#check if session id matches
            if (item_buf):#if value in buf
                session_dic[pre_sid] = (items2vec(_df_item,item_buf))#calculate item_vecs for session
            pre_sid = row[1].session_id# move to next session
            item_buf=[]
        item_buf.append(row[1].item_id)
    session_dic[pre_sid] = (items2vec(_df_item,item_buf))#saving last session vec 
    e_t=time.time()
    df = pd.DataFrame(session_dic).T
    df.columns = _df_item.columns
    df = df.reset_index()
    df = df.rename(columns = {"index":"session_id"})
    #print(df.head())
    print("total session: ",len(session_dic)," time usage: ",e_t-s_t," sec")
    return df
if __name__ =="__main__":
    session_path = sys.argv[1]
    item_path = (sys.argv[2])
    sessions2vec(item_path,session_path).to_csv(sys.argv[3])
    
