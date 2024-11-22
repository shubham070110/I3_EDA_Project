import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('student-por.csv')
# print(df.head(10))

# print(df.info())
# print(df.duplicated().sum())
# print(df.isnull().sum())

# cats = [col for col in df.columns if df[col].dtype == 'object']
# print("categorical data",cats)

# nums = [col for col in df.columns if df[col].dtype != 'object']
# print("numerical data",nums)

# plt.figure(figsize = (8,5))
# sns.countplot(x = 'school' , data=df , palette='viridis')
# plt.title('dist of schools')
# plt.xlabel('school')
# plt.ylabel('count')
# plt.show()

# sns.histplot(df['age'], bins = 20  , kde = True)
# plt.show()

# sns.countplot(x ='address' ,data = df, palette='dark')
# plt.show()

# reason_count = df['reason'].value_counts()
# plt.pie(reason_count,autopct="%1.1f%%", labels = reason_count.index)
# plt.show()

# acti_count = df['activities'].value_counts()
# plt.pie(acti_count,autopct="%1.1f%%" , labels = acti_count.index)
# plt.show()

# sns.boxplot(x = 'Fjob', y = 'Mjob' ,data = df , palette='coolwarm' )
# plt.show()

# alc = df['Walc'].value_counts()
# plt.pie(alc,autopct = '%1.1f%%',labels=alc.index)
# plt.show()

# dalc = df['Dalc'].value_counts()
# plt.pie(dalc , autopct = '%1.1f%%',labels=dalc.index)
# plt.show()

# bivariate analysis

# plt.figure(figsize=(12,6))
# plt.subplot(1,2,1)
# sns.countplot(x = 'Medu',hue = 'Fjob',data = df,palette = 'viridis')
# plt.title('mother education level')
# plt.xlabel('mother ed level')
# plt.ylabel('count')
# plt.show()


plt.subplot(1,2,2)
sns.countplot(x = 'Fedu',data = df,palette = 'viridis')
plt.title('father education level')
plt.xlabel('father ed level')
plt.ylabel('count')

# plt.show()

# sns.barplot(x = 'studytime' , y= 'G3',data = df)
# plt.title('student study time')
# plt.xlabel('study')
# plt.ylabel('hourse')
# plt.show()

# sns.barplot(x = 'internet' , y = 'G3',data = df)
# plt.title('internet study time')
# plt.xlabel('internet')
# plt.ylabel('hourse')
# plt.show()

# sns.barplot(x='studytime' , y = 'G3',data = df)
# plt.show()

# sns.barplot(x = 'studytime' , y = 'G2' , data = df)
# plt.show()

# sns.barplot(x = 'studytime' , y = 'G1' , data = df)
# plt.show()

# multivariate analysis

# sns.barplot(x = 'sex' , y = 'G3' , hue = "address",data = df, palette='viridis')
# plt.show()

# num_cols = ['age', 'traveltime','studytime','absences','G1','G2','G3']
# sns.boxplot(data = df[num_cols], palette='coolwarm')
# plt.show()

# corr = df.corr(numeric_only= True)
# sns.heatmap(corr,annot = True,cmap = 'coolwarm',fmt = '.2f')
# plt.show()

# print(df.info())

# for i in df.columns:
#     if df[i].dtype == 'object':
#         print(f"columns name {i} --> {df[i].unique()}")


# for i in df.columns:
#     if df[i].dtype != 'object':
#         print(f"columns name {i} --> {df[i].unique()}")






