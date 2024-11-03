import kagglehub
path = kagglehub.dataset_download("henriqueyemahata/bank-marketing")
print("Downloaded to:",path)
data = pd.read_csv(path+"/bank-additional-full.csv",sep=";")
df=pd.DataFrame(data)
print(df.head())
print(df.isnull().sum())