# 要添加一个新单元，输入 '# %%'
# 要添加一个新的标记单元，输入 '# %% [markdown]'
# %%
import pandas as pd 
import numpy as np 
pd.set_option('display.max_columns', None)
df1=pd.read_excel(r"D:\cardiac arrest\gut-CA\original_material\patient_lab_result.xlsx")


# %%
df2=pd.read_csv(r"D:\cardiac arrest\gut-CA\second_result(sorted)\data_c.csv", encoding = 'gb2312')
df_lab=pd.read_csv(r"D:\cardiac arrest\gut-CA\second_result(sorted)\合并检验数据.csv")


# %%
df2['PATIENT_']=df2['ID']
df_merged=pd.merge(df2, df_lab, on=['PATIENT_'], how='outer')
df_merged=df_merged.applymap(lambda x: np.NaN if str(x).isspace() else x)
df_merged.head()


# %%
df_alt=df_merged.iloc[:,57:64:1]
df_aptt=df_merged.iloc[:,64:71:1]
df_ast=df_merged.iloc[:,71:78:1]
df_bnp=df_merged.iloc[:,78:85:1]
df_ck=df_merged.iloc[:,85:92:1]
df_ckmb=df_merged.iloc[:,92:97:1]
df_crp=df_merged.iloc[:,97:104:1]
df_ddimer=df_merged.iloc[:,104:111:1]
df_fib=df_merged.iloc[:,111:118:1]
df_glu=df_merged.iloc[:,118:125:1]
df_hb=df_merged.iloc[:,125:132:1]
df_jigan=df_merged.iloc[:,132:139:1]
df_k=df_merged.iloc[:,139:146:1]
df_lip=df_merged.iloc[:,146:153:1]
df_na=df_merged.iloc[:,153:160:1]
df_neu=df_merged.iloc[:,160:167:1]
df_pct=df_merged.iloc[:,167:174:1]
df_plt=df_merged.iloc[:,174:181:1]
df_pta=df_merged.iloc[:,181:188:1]
df_ra=df_merged.iloc[:,188:195:1]
df_rbc=df_merged.iloc[:,195:202:1]
df_tb=df_merged.iloc[:,202:209:1]
df_tni=df_merged.iloc[:,209:216:1]
df_wbc=df_merged.iloc[:,216:223:1]


df_aptt=df_aptt.reindex(columns=['aptt0h','aptt4h','aptt8h','aptt12h','aptt24h', 'aptt48h', 'aptt72h'])
df_ast=df_ast.reindex(columns=['ast0h','ast4h','ast8h','ast12h','ast24h', 'ast48h', 'ast72h'])
df_bnp=df_bnp.reindex(columns=['bnp0h','bnp4h','bnp8h','bnp12h','bnp24h', 'bnp48h', 'bnp72h'])
df_ck=df_ck.reindex(columns=['ck0h','ck4h','ck8h','ck12h','ck24h', 'ck48h', 'ck72h'])
df_ckmb=df_ckmb.reindex(columns=['ckmb0h','ckmb4h','ckmb8h','ckmb12h','ckmb24h', 'ckmb48h', 'ckmb72h'])
df_crp=df_crp.reindex(columns=['crp0h','crp4h','crp8h','crp12h','crp24h', 'crp48h', 'crp72h'])
df_ddimer=df_ddimer.reindex(columns=['ddimert0h','ddimert4h','ddimert8h','ddimert12h','ddimert24h','ddimert48h','ddimert72h'])
df_fib=df_fib.reindex(columns=['fib0h','fib4h','fib8h','fib12h','fib24h','fib48h','fib72h'])
df_glu=df_glu.reindex(columns=['glu0h','glu4h','glu8h','glu12h','glu24h','glu48h','glu72h'])
df_hb=df_hb.reindex(columns=['hb0h','hb4h','hb8h','hb12h','hb24h','hb48h','hb72h'])
df_jigan=df_jigan.reindex(columns=['jigan0h','jigan4h','jigan8h','jigan12h','jigan24h','jigan48h','jigan72h'])
df_k=df_k.reindex(columns=['k0h','k4h','k8h','k12h','k24h','k48h','k72h'])
df_lip=df_lip.reindex(columns=['lip0h','lip4h','lip8h','lip12h','lip24h','lip48h','lip72h'])
df_na=df_na.reindex(columns=['na0h','na4h','na8h','na12h','na24h','na48h','na72h'])
df_neu=df_neu.reindex(columns=['neu0h','neu4h','neu8h','neu12h','neu24h','neu48h','neu72h'])
df_pct=df_pct.reindex(columns=['pct0h','pct4h','pct8h','pct12h','pct24h','pct48h','pct72h'])
df_plt=df_plt.reindex(columns=['plt0h','plt4h','plt8h','plt12h','plt24h','plt48h','plt72h'])
df_pta=df_pta.reindex(columns=['pta0h','pta4h','pta8h','pta12h','pta24h','pta48h','pta72h'])
df_ra=df_ra.reindex(columns=['ra0h','ra4h','ra8h','ra12h','ra24h','ra48h','ra72h'])
df_rbc=df_rbc.reindex(columns=['rbc0h','rbc4h','rbc8h','rbc12h','rbc24h','rbc48h','rbc72h'])
df_tb=df_tb.reindex(columns=['tb0h','tb4h','tb8h','tb12h','tb24h','tb48h','tb72h'])
df_tb


# %%
def get_col_name(s):
    try:
        idx=s.loc[s.notna()].index[0]
        return s.loc[idx]
    except:
        return np.nan

df_merged['alt(first_na)']=df_alt.apply(lambda s: get_col_name(s), axis=1)
df_merged['aptt(first_na)']=df_aptt.apply(lambda s: get_col_name(s), axis=1)
df_merged['ast(first_na)']=df_ast.apply(lambda s: get_col_name(s), axis=1)
df_merged['bnp(first_na)']=df_bnp.apply(lambda s: get_col_name(s), axis=1)
df_merged['ck(first_na)']=df_ck.apply(lambda s: get_col_name(s), axis=1)
df_merged['ckmb(first_na)']=df_ckmb.apply(lambda s: get_col_name(s), axis=1)
df_merged['crp(first_na)']=df_crp.apply(lambda s: get_col_name(s), axis=1)
df_merged['ddimer(first_na)']=df_ddimer.apply(lambda s: get_col_name(s), axis=1)
df_merged['fib(first_na)']=df_fib.apply(lambda s: get_col_name(s), axis=1)
df_merged['glu(first_na)']=df_glu.apply(lambda s: get_col_name(s), axis=1)
df_merged['hb(first_na)']=df_hb.apply(lambda s: get_col_name(s), axis=1)
df_merged['jigan(first_na)']=df_jigan.apply(lambda s: get_col_name(s), axis=1)
df_merged['k(first_na)']=df_k.apply(lambda s: get_col_name(s), axis=1)
df_merged['lip(first_na)']=df_lip.apply(lambda s: get_col_name(s), axis=1)
df_merged['na(first_na)']=df_na.apply(lambda s: get_col_name(s), axis=1)
df_merged['neu(first_na)']=df_neu.apply(lambda s: get_col_name(s), axis=1)
df_merged['pct(first_na)']=df_pct.apply(lambda s: get_col_name(s), axis=1)
df_merged['plt(first_na)']=df_plt.apply(lambda s: get_col_name(s), axis=1)
df_merged['pta(first_na)']=df_pta.apply(lambda s: get_col_name(s), axis=1)
df_merged['ra(first_na)']=df_ra.apply(lambda s: get_col_name(s), axis=1)
df_merged['rbc(first_na)']=df_rbc.apply(lambda s: get_col_name(s), axis=1)
df_merged['tb(first_na)']=df_tb.apply(lambda s: get_col_name(s), axis=1)
df_merged['tni(first_na)']=df_tni.apply(lambda s: get_col_name(s), axis=1)
df_merged['wbc(first_na)']=df_wbc.apply(lambda s: get_col_name(s), axis=1)


df_merged.tail()


# %%
df_toxin=pd.read_csv(r"D:\cardiac arrest\gut-CA\second_result(sorted)\toxin.csv")
df_toxin['ID']=df_toxin['ID号']
df_total=pd.merge(df_toxin,df_merged, on=['ID'], how='inner')  
df_total.head()


# %%
df_toxin.head()


# %%
file = open(r"D:\cardiac arrest\gut-CA\second_result(sorted)\126_all_variables.xlsx")
outputpath=r"D:\cardiac arrest\gut-CA\second_result(sorted)\126_all_variables.xlsx"
df_total.to_excel(r"D:\cardiac arrest\gut-CA\second_result(sorted)\126_all_variables.xlsx", sheet_name='Sheet1', na_rep='',
 float_format=None, columns=None, header=True, index=True, 
 index_label=None, startrow=0, startcol=0, engine=None, 
 merge_cells=True, encoding=None, inf_rep='inf', verbose=True, 
 freeze_panes=None)


# %%
x=((df_total.isnull().sum())/df_merged.shape[0]).sort_values(ascending=False).map(lambda x:"{:.2%}".format(x))
x


