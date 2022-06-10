from scipy.sparse import csr_matrix
import pandas as pd
import time
import sys
import numpy as np
import itertools
sys.argv

def seq2pair(seq_lst):
    unique_names = set(itertools.chain.from_iterable(seq_lst))
    all_pairs = list(itertools.combinations(unique_names, 2))
    return all_pairs
def seq_target2pair(_df_s,_df_t):
    
    return


def sess2item_co_occur(session_path,):
    '''
    input 1 path to session.csv
    '''
    s_t = time.time()
    _df_session = pd.read_csv(session_path)
    pre_sid = None
    items_buf=[]
    re_data = []
    for row in _df_session.iterrows():#tuple of row value,row[0]=index,row[1]=values
        if pre_sid!=row[1].session_id:#check if session id matches
            if (items_buf):#if value in buf
                re_data+=[seq2pair([items_buf])]#calculate item_vecs for session
            pre_sid = row[1].session_id# move to next session
            items_buf=[]
        items_buf.append(row[1].item_id)
    re_data+=[seq2pair([items_buf])]
    #flatten 2d list to 1d(re_data)
    re_data = list(itertools.chain.from_iterable(re_data))
    df = pd.DataFrame(re_data, columns=['item1', 'item2'])
    #bulding co occurence table
    i, r = pd.factorize(df['item1'])
    j, c = pd.factorize(df['item2'])
    ij, tups = pd.factorize(list(zip(i, j)))
    a = csr_matrix((np.bincount(ij), tuple(zip(*tups))))
    b = pd.DataFrame.sparse.from_spmatrix(a, r, c).sort_index().sort_index(axis=1) 
    e_t=time.time()
    print("co-occurence table shape: ",b.shape," time usage: ",e_t-s_t," sec")
    b = b.reset_index().rename(columns={"index":"item_id"})
    return b

if __name__ =="__main__":
    #sess2item_co_occur(sys.argv[1]).to_csv(sys.argv[2],index=False)
    print("done")
