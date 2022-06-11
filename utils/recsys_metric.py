import pandas as pd

def mrr(evaluation_df, label_df, overview=True):
    """
    ++++++++++++++++++++++++++++++++++++
    
    `evaluation_df` example:
        | session_id | item_id | rank |
        |-----------:|--------:|-----:|
        |          3 |   16958 |   96 |
        |          3 |    2848 |   97 |
        |          3 |   12127 |   98 |
        |          3 |   23167 |   99 |
        |          3 |   26253 |  100 |
        |         13 |   27714 |    1 |
        |         13 |    5433 |    2 |
        |         13 |   21107 |    3 |
        |         13 |   21215 |    4 |
        |         13 |    2410 |    5 |
    ++++++++++++++++++++++++++++++++++++
    
    `label_df` example:
        | session_id | item_id |
        |-----------:|--------:|
        |          3 |   15085 |
        |         13 |   18626 |
        |         18 |   24911 |
        |         19 |   12534 |
        |         24 |   13226 | 
    ++++++++++++++++++++++++++++++++++++
    """
    match_filter = pd.merge(evaluation_df, label_df, on=['session_id', 'item_id'])
    rank_arr = pd.merge(label_df, match_filter, how='left', on=['session_id'], suffixes=["","_m"]).loc[:,["session_id", "item_id", "rank"]]
    rank_arr['r_rank'] = 1/rank_arr['rank']
    rank_arr = rank_arr.fillna(0)
    mrr = rank_arr['r_rank'].sum()/len(label_df)
    
    if (overview):
        display(match_filter.head(), rank_arr.head(50))
        
    return mrr