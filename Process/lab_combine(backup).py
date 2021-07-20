# It is a second way to get non-NA lab result
import pandas as pd 
import numpy as np 
pd.set_option('display.max_columns', None)
df1=pd.read_excel(r"D:\cardiac arrest\gut-CA\original_material\patient_lab_result.xlsx")


# %%
df2=pd.read_csv(r"D:\cardiac arrest\gut-CA\data_c.csv",encoding = 'gb2312')


# %%
df_lab=pd.read_csv(r"D:\cardiac arrest\gut-CA\合并检验数据.csv")


# %%
df_lab.head()


# %%
df2['PATIENT_']=df2['ID']


# %%
df_merged=pd.merge(df2, df_lab, on=['PATIENT_'], how='inner')


# %%
df_merged=df_merged.applymap(lambda x: np.NaN if str(x).isspace() else x)




# %%
df_merged['base_alt']=df_merged["alt0h"]
df_merged["base_alt"]=df_merged["base_alt"].fillna(df_merged["alt4h"],inplace=True)
df_merged["base_alt"].fillna(df_merged["alt4h"],inplace=True)

df_merged['base_aptt']=df_merged["aptt0h"]
df_merged["base_aptt"]=df_merged["base_aptt"].fillna(df_merged["aptt4h"],inplace=True)
df_merged["base_aptt"].fillna(df_merged["aptt8h"],inplace=True)

df_merged['base_ast']=df_merged["ast0h"]
df_merged["base_ast"]=df_merged["base_ast"].fillna(df_merged["ast4h"],inplace=True)
df_merged["base_ast"].fillna(df_merged["ast8h"],inplace=True)

df_merged['base_bnp']=df_merged["bnp0h"]
df_merged["base_bnp"]=df_merged["base_bnp"].fillna(df_merged["bnp4h"],inplace=True)
df_merged["base_bnp"].fillna(df_merged["bnp8h"],inplace=True)

df_merged['base_ck']=df_merged["ck0h"]
df_merged["base_ck"]=df_merged["base_ck"].fillna(df_merged["ck4h"],inplace=True)
df_merged["base_ck"].fillna(df_merged["ck8h"],inplace=True)

df_merged['base_ckmb']=df_merged["ckmb0h"]
df_merged["base_ckmb"]=df_merged["base_ckmb"].fillna(df_merged["ckmb4h"],inplace=True)
df_merged["base_ckmb"].fillna(df_merged["ckmb8h"],inplace=True)

df_merged['base_crp']=df_merged["crp0h"]
df_merged["base_crp"]=df_merged["base_crp"].fillna(df_merged["crp4h"],inplace=True)
df_merged["base_crp"].fillna(df_merged["crp8h"],inplace=True)

df_merged['base_ddimer']=df_merged["ddimert0h"]
df_merged["base_ddimer"]=df_merged["base_ddimer"].fillna(df_merged["ddimert4h"],inplace=True)
df_merged["base_ddimer"].fillna(df_merged["ddimert8h"],inplace=True)

df_merged['base_fib']=df_merged["fib0h"]
df_merged["base_fib"]=df_merged["base_fib"].fillna(df_merged["fib4h"],inplace=True)
df_merged["base_fib"].fillna(df_merged["fib8h"],inplace=True)

df_merged['base_glu']=df_merged["glu0h"]
df_merged["base_glu"]=df_merged["base_glu"].fillna(df_merged["glu4h"],inplace=True)
df_merged["base_glu"].fillna(df_merged["glu8h"],inplace=True)


df_merged['base_hb']=df_merged["hb0h"]
df_merged["base_hb"]=df_merged["base_hb"].fillna(df_merged["hb4h"],inplace=True)
df_merged["base_hb"].fillna(df_merged["hb8h"],inplace=True)


df_merged['base_Cr']=df_merged["jigan0h"]
df_merged["base_Cr"]=df_merged["base_Cr"].fillna(df_merged["jigan4h"],inplace=True)
df_merged["base_Cr"].fillna(df_merged["jigan8h"],inplace=True)

df_merged['base_k']=df_merged["k0h"]
df_merged["base_k"]=df_merged["base_k"].fillna(df_merged["k4h"],inplace=True)
df_merged["base_k"].fillna(df_merged["k8h"],inplace=True)



df_merged['base_lip']=df_merged["lip0h"]
df_merged["base_lip"]=df_merged["base_lip"].fillna(df_merged["lip4h"],inplace=True)
df_merged["base_lip"].fillna(df_merged["lip8h"],inplace=True)

df_merged['base_na']=df_merged["na0h"]
df_merged["base_na"]=df_merged["base_na"].fillna(df_merged["na4h"],inplace=True)
df_merged["base_na"].fillna(df_merged["na8h"],inplace=True)

df_merged['base_neu']=df_merged["neu0h"]
df_merged["base_neu"]=df_merged["base_neu"].fillna(df_merged["neu4h"],inplace=True)
df_merged["base_neu"].fillna(df_merged["neu8h"],inplace=True)


df_merged['base_pct']=df_merged["pct0h"]
df_merged["base_pct"]=df_merged["base_pct"].fillna(df_merged["pct4h"],inplace=True)
df_merged["base_pct"].fillna(df_merged["pct8h"],inplace=True)


df_merged['base_plt']=df_merged["plt0h"]
df_merged["base_plt"]=df_merged["base_plt"].fillna(df_merged["plt4h"],inplace=True)
df_merged["base_plt"].fillna(df_merged["plt8h"],inplace=True)

df_merged['base_pta']=df_merged["pta0h"]
df_merged["base_pta"]=df_merged["base_pta"].fillna(df_merged["pta4h"],inplace=True)
df_merged["base_pta"].fillna(df_merged["pta8h"],inplace=True)



df_merged['base_ra']=df_merged["ra0h"]
df_merged["base_ra"]=df_merged["base_ra"].fillna(df_merged["ra4h"],inplace=True)
df_merged["base_ra"].fillna(df_merged["ra8h"],inplace=True)


df_merged['base_rbc']=df_merged["rbc0h"]
df_merged["base_rbc"]=df_merged["base_rbc"].fillna(df_merged["rbc4h"],inplace=True)
df_merged["base_rbc"].fillna(df_merged["rbc8h"],inplace=True)


df_merged['base_tb']=df_merged["tb0h"]
df_merged["base_tb"]=df_merged["base_tb"].fillna(df_merged["tb4h"],inplace=True)
df_merged["base_tb"].fillna(df_merged["tb8h"],inplace=True)

df_merged['base_tni']=df_merged["tni0h"]
df_merged["base_tni"]=df_merged["base_tni"].fillna(df_merged["tni4h"],inplace=True)
df_merged["base_tni"].fillna(df_merged["tni8h"],inplace=True)


df_merged['base_wbc']=df_merged["wbc0h"]
df_merged['base_wbc']=df_merged["base_wbc"].fillna(df_merged["wbc4h"],inplace=True)
df_merged["base_wbc"].fillna(df_merged["wbc8h"],inplace=True)



# %%
x=((df_merged.isnull().sum())/df_merged.shape[0]).sort_values(ascending=False).map(lambda x:"{:.2%}".format(x))

pd.set_option('display.max_rows', None)
x


