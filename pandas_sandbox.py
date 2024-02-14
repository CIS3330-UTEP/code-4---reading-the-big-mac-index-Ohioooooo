import pandas as pd

#list_teams = ['49ers','Kansas City','Cowboys','Packers']

#print(type(list_teams))

#series_teams = pd.Series(list_teams)

#print(series_teams)
#print(type(series_teams))

#students = {'Ohio':'David','Hawai':'Isabella','Iowa':'Roberto'}
#print(type(students))
#print(students)

#student_series = pd.Series(index=students.keys(),data=student.keys,data))

#print(student_series)
#print(type(student_series))

df = pd.read_csv('big-mac-full-index.csv')

#print(type(df))
#print(df.columns)
#print(type(df.columns))

#print(df)
#print(df['name'])
#print(type(df['name']))

#query_text = f"iso_a3 == 'MEX' "
country_code = ['MEX']
query_text = f"iso_a3 == @country_code"

df_mex = df.query(query_text)
print(df_mex)

#print(round(df_mex['local_price'].mean(),2))
#print(df_mex['local_price'].median())
#print(df_mex['dollar_price'].min())
#print(df_mex['dollar_price'].max())

idx_dollar_price = df_mex['dollar_price'].idxmin()

mex_series = df_mex.loc[idx_dollar_price]

print(mex_series)