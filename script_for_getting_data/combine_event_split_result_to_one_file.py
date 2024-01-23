import pandas as pd

filenames = ["event_split_result/split"+str(i)+"_result.csv" for i in range(1, 29)]

df_list = []

for filename in filenames:
    df_list.append(pd.read_csv(filename))

combined_df = pd.concat(df_list)

combined_df.to_csv('all_user_event_data.csv', index=False)  