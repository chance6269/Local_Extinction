# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:42:45 2024

@author: Shin
"""
#%%
# 충북
import pandas as pd
city = ['uni', 'junior_sc', 'middle_sc', 'high_sc'] 

csv_file_paths = []

for sc_type in city:
    
    df = pd.read_csv(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/csv_data/{sc_type}.csv")
    df = df.drop(columns=['Unnamed: 0'])
    df = df.loc[10]
    df = df[1:]

    df.to_csv(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungbuk_data/{sc_type}.csv", index=False, header=False)   
   
    csv_file_paths.append(df)
#%%
#충북
edu = pd.read_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/csv_data/chungbuk_edu.csv")
edu = edu.drop(index=0 & 1)
edu = edu.transpose()
edu = edu.iloc[1:]
edu.reset_index()
#edu.columns = ['개수']

edu.to_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungbuk_data/chungbuk.csv",index=False, header=False)

#%%
cit = ['uni', 'junior_sc', 'middle_sc', 'high_sc','chungbuk']    


combined_df = pd.DataFrame()

for file in cit :
    df = pd.read_csv(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungbuk_data/{file}.csv", header=None)  # 파일을 읽어오기
    if combined_df.empty:
        combined_df = df
    else:
        combined_df += df

# 결과를 CSV 파일로 저장
combined_df.to_csv('result_chungbuk.csv', header=False)





#%%

#df_daegeon = df.iloc[[5]]
#df_sejong = df.iloc[[7]]
#df_chungbuk = df.iloc[[10]]
#df_chungnam = df.iloc[[11]]

    
#%%
# 세종
city = ['uni', 'junior_sc', 'middle_sc', 'high_sc'] 

csv_file_paths = []

for sc_type in city:
    
    df = pd.read_csv(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/csv_data/{sc_type}.csv")
    df = df.drop(columns=['Unnamed: 0'])
    df = df.loc[7]
    df = df[1:]

    df.to_csv(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/sejong_data/{sc_type}.csv", index=False, header=False)   
    
    csv_file_paths.append(df)
#%%    
# 세종
edu = pd.read_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/csv_data/sejong_edu.csv")
edu = edu.drop(index=0 & 1)
edu = edu.transpose()
edu = edu.iloc[1:]
edu.to_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/sejong_data/sejong.csv", index=False, header=False)
#%%
combined_df = pd.DataFrame()


cit = ['uni', 'junior_sc', 'middle_sc', 'high_sc', 'sejong']    

for file in cit :
    df = pd.read_csv(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/sejong_data/{file}.csv", header=None)  # 파일을 읽어오기
    if combined_df.empty:
        combined_df = df
    else:
        combined_df += df

# 결과를 CSV 파일로 저장
combined_df.to_csv('result_sejong.csv',header=False)

#%%
# 충남
city = ['uni', 'junior_sc', 'middle_sc', 'high_sc'] 

csv_file_paths = []

for sc_type in city:
    
    df = pd.read_csv(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/csv_data/{sc_type}.csv")
    df = df.drop(columns=['Unnamed: 0'])
    df = df.loc[11]
    df = df[1:]
  
    df.to_csv(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungnam_data/{sc_type}.csv", index=False, header=False)   
    
    csv_file_paths.append(df)
    
#%%   
# 충남
edu = pd.read_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/csv_data/chungnam_edu.csv")
edu = edu.drop(index=0 & 1)
edu = edu.transpose()
edu = edu.iloc[1:]
edu.to_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungnam_data/chungnam.csv", index=False, header=False)

#%%
combined_df = pd.DataFrame()


cit = ['uni', 'junior_sc', 'middle_sc', 'high_sc', 'chungnam']    

for file in cit :
    df = pd.read_csv(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungnam_data/{file}.csv", header=None)  # 파일을 읽어오기
    if combined_df.empty:
        combined_df = df
    else:
        combined_df += df

# 결과를 CSV 파일로 저장
combined_df.to_csv('result_chungnam.csv', header=False)