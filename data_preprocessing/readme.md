# file info
## item_vector.pkl

使用以下code讀檔。
````python
file = open("item_vector.pkl", "rb")
output = pickle.load(a_file) # It's a dict
file.close()
````
output 為一 `dict`，key為item_id，value為list，內容為one-hot-encoding的結果。
關於one-hot-encoding內容可以參考`all_feature_encoding.csv`
若[item_id]有該特徵，ouput[item_id][label]=1，若無則等於0
