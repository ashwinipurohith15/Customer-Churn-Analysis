#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Reading the data
customers_df= pd.read_csv("customers.csv")
customers_df.head()


# In[2]:


customers_df.info()


# In[3]:


customers_df.describe()


# In[14]:


churn_df= pd.read_csv("churn.csv")
churn_df.head()


# In[9]:


Subscriptions_df= pd.read_csv("Subscriptions.csv")
Subscriptions_df.head()


# In[12]:


Transactions_Data= pd.read_csv("Transactions.csv")
Transactions_Data.head()


# In[16]:


#1. Print first 5 customers FirstNames and LastNames

Customer_names= customers_df[['FirstName','LastName']]
Customer_names.head()


# In[23]:


#2. Find out customers from specific Region (North America)

Customer_Region=customers_df[customers_df['Region']== 'North America']
Customer_Region.head()
print(Customer_Region)


# In[26]:


#3. Find customers in specific Regions (Europe or Asia)

Customer_region=customers_df[customers_df['Region'].isin(['Europe','Asia'])]
print(Customer_region)


# In[29]:


#4. Find Customers with Active Status

status= customers_df[customers_df['Status']== 'Active']
status.head()
print(status)


# In[31]:


#5. Visualization of Active & Inactive Customers

#Calculate the number of active / Inactive customers

status_count=customers_df['Status'].value_counts()

#Create a pie chart to show the distribution

plt.figure(figsize=(8,6))
plt.pie(status_count, labels=status_count.index, autopct='%1.1f%%', colors=['#66c2a5','#fc8d62'])
plt.title('Distribution of Customer Status')
plt.show()


# In[36]:


#6. List down the customers who joined after '2020-01-01'
#convert the 'JoinDate' column to date time format
customer_joined=customers_df[pd.to_datetime(customers_df['JoinDate'],format='%d-%m-%Y')>'2020-01-01']
print(customer_joined)


# In[39]:


#7. Create a visualisation(bar chart) who joined after and befoe 2021
 #converting JoinDate into DATE TIME FORMAT
customers_df['JoinDate']=pd.to_datetime(customers_df['JoinDate'],format='%d-%m-%Y')

# Filtering the customers who joined before and after 2021

before_2021=customers_df[customers_df['JoinDate']<'2021-01-01']
after_2021=customers_df[customers_df['JoinDate']>'2021-01-01']

# Count the number of customers in each of the category
counts={'Before 2021': len(before_2021),'After 2021': len(after_2021)}

# create a bar chart
plt.bar(counts.keys(),counts.values(), color=['blue','green'])
plt.xlabel('Join Date Category')
plt.ylabel('No. of customers')
plt.title('Customers who joined before and after 2021')


#Add the exact numbers on the top of the bars
for i, (key,value) in enumerate(counts.items()):
    plt.text(i,value+0.5, str(value), ha='center', fontsize=12)
plt.show()

# Using for loop, the loop goes through each bar (Before 2021 and After 2021)
#For each bar, it places the customer count(value) as a label slightly above the bar, position it at centre
#counts.items(): This gives you both the key and the values from dictionary


# In[ ]:





# In[44]:


#8. List down the active customers from Europe
Active_cx=customers_df[(customers_df['Region']=='Europe') & (customers_df['Status']=='Active')]
result=len(Active_cx)
print(result)


# In[49]:


#Visualisation of active and Inactive Customers in Europe.
# Filtering the european customers
customers_europe=customers_df[customers_df['Region']=='Europe']

#Count the number of active and Inactive 
status_counts= customers_europe['Status'].value_counts()

plt.figure(figsize=(8,6))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%',colors=['pink','purple'])
plt.title('Distribution of Customers')
plt.show()


# In[101]:


customers_df['JoinDate']=pd.to_datetime(customers_df['JoinDate'],format='%d-%m-%Y')
customers_df['Joined2021'] = pd.to_datetime(customers_df['JoinDate']).dt.year == 2021

# Count the number of customers who are in yes or no
joined_2021_counts = customers_df['Joined2021'].value_counts()

# Create a bar chart
plt.figure(figsize=(8, 6))
joined_2021_counts.plot(kind='bar', color=['red', 'green'], edgecolor='black')
plt.xlabel('Joined in 2021')
plt.ylabel('Count')
plt.title('Bar Chart Comparison of Customers Who Joined in 2021')
plt.xticks(ticks=[0, 1], labels=['No', 'Yes'], rotation=0)
plt.tight_layout()

plt.show()


# In[95]:


customers_df.info()


# In[98]:


customers_df.describe()


# In[102]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Reading the data
Transactions_df= pd.read_csv("Transactions.csv")
Transactions_df.head()


# In[103]:


#calculate the average transaction amount
Average_amount= Transactions_df['Amount'].mean()
print(f"Average Transaction Amount: {Average_amount}")


# In[111]:


# Visualize / Analysis for Transaction Amount w.r.t to Index - Line graph
plt.figure(figsize=(12, 6))
plt.plot(Transactions_df.index, Transactions_df['Amount'],linestyle='-', linewidth=2, color='blue')

plt.title('Transaction Amount VS Index')
plt.xlabel('Transaction Index')
plt.ylabel('Transaction Amount')
plt.grid(True)
plt.show()


# In[116]:


# Visualize / Analysis for Transaction Amount w.r.t to Index - scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(Transactions_df.index, Transactions_df['Amount'],color='Green')

plt.title('Transaction Amount VS Index')
plt.xlabel('Transaction Index')
plt.ylabel('Transaction Amount')
plt.grid(True)
plt.show()


# In[118]:


# Transactions which are more than $100
Max_amount= Transactions_df[Transactions_df['Amount']>100]
print(Max_amount)


# In[121]:


# Using a pie chart .. show me the % breakdown of  "Above $100 and Below / Equal to $100
above_100= Transactions_df[Transactions_df['Amount']>100].shape[0]
Below_or_equal_100 = Transactions_df[Transactions_df['Amount']<=100].shape[0]

labels= ['Above 100', 'Below or Equal to 100']
sizes= [above_100, Below_or_equal_100]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')


# In[122]:


# Bar chart .. "Transactions Categories" Vs "No. of Transcations"

above_100= Transactions_df[Transactions_df['Amount']>100].shape[0]
Below_or_equal_100 = Transactions_df[Transactions_df['Amount']<=100].shape[0]

# Count the number of customers in each of the category
counts={'Above 100': above_100,
       'Below or equal to 100' : Below_or_equal_100}

# create a bar chart
plt.bar(counts.keys(),counts.values(), color=['blue','green'])
plt.xlabel('Above 100')
plt.ylabel('Below or equal to 100')
plt.title('Customers who joined before and after 2021')


#Add the exact numbers on the top of the bars
for i, (key,value) in enumerate(counts.items()):
    plt.text(i,value+0.5, str(value), ha='center', fontsize=12)
plt.show()


# In[126]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Reading the data
Churn_df= pd.read_csv("Churn.csv")
Churn_df.head()


# In[127]:


#Find the number of customers who left the company/ churned for each reason
reason_counts=Churn_df['Reason'].value_counts
print(reason_counts)


# In[134]:


# Visualization of Churned vs Not Churned customers 
#Assuming we have a "Status" column indicating "Churn" and "Not Churned"

total_customers=customers_df.shape[0]
total_churned_customers=Churn_df.shape[0]
total_not_churned_customers= total_customers - total_churned_customers

#going to represent the two categories
status= pd.DataFrame({
    'Status': ['Churned', 'Not Churned'],
    'Count' : [total_churned_customers, total_not_churned_customers]
})

#Bar Chart
plt.figure(figsize=(10,6))
sns.barplot(x='Status',y='Count', data= status, palette='Set1', hue='Status',legend=False)
plt.xlabel('Customer Status')
plt.ylabel('No. of Customers')
plt.title('Churned Vs Not Churned')
plt.tight_layout()
plt.show()


# In[136]:


plt.figure(figsize=(10,6))
plt.pie(status['Count'],labels=status['Status'],autopct='%1.1f%%',startangle=90, colors=sns.color_palette('Set1'))
plt.title('Churned Vs Not Churned')
plt.tight_layout()
plt.show()


# In[139]:


#List Churn Reasons with Service"
#Filter the 'Churn_df' dataframe to include only rows where the "reason" column contains the word "Service"

service_reasons= Churn_df[Churn_df['Reason'].str.contains('service', case=False, na=False)]
print(service_reasons[['CustomerID','Reason']])


# In[140]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Reading the data
Subscriptions_df=pd.read_csv("Subscriptions.csv")
Subscriptions_df.head()


# In[144]:


# Join Customers and Subscriptions
join_df= pd.merge(customers_df, Subscriptions_df, on='CustomerID', how='inner')
print(join_df)


# In[146]:


#visualization for different Customer Groups [Active-Annual, Active-monthly, Inactive-Annual, Inactive-Monthly]
result= customers_df.merge(Subscriptions_df,on='CustomerID')
result['flag'] = result['Status']+" "+result['PlanType']
data=result.groupby('flag', as_index=False).agg(total_cnt=('CustomerID','count'))
plt.figure(figsize=(6,6))
plt.pie(data['total_cnt'],labels=data['flag'],autopct="%1.1f%%", startangle=140)
plt.title("Churned Types")
plt.show()


# In[10]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

Transactions_df= pd.read_csv("Transactions.csv")
Transactions_df.head()


# In[11]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

customers_df= pd.read_csv("customers.csv")
customers_df.head()


# In[10]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

Transactions_df= pd.read_csv("Transactions.csv")
Transactions_df.head()


# In[12]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

Subscriptions_df= pd.read_csv("Subscriptions.csv")
Subscriptions_df.head()


# In[13]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

Churn_df= pd.read_csv("Churn.csv")
Churn_df.head()


# In[14]:


#EDA - Exploratory Data Analysis 
#Data Cleaning
# Merge All Datasets

merged_df= pd.merge(customers_df, Subscriptions_df,on='CustomerID', how='left')
merged_df=pd.merge(merged_df,Transactions_df,on='CustomerID',how='left')
final_df=pd.merge(merged_df,Churn_df,on='CustomerID',how='left')
#Display the result
final_df.head()


# In[15]:


final_df.shape


# In[16]:


#Add a column named as "churned" based on the presence of "churnID"
final_df['Churned']=final_df['ChurnID'].apply(lambda x:1 if pd.notna(x)else 0)
final_df.head()


# In[156]:


#Delete Missing values
missing_values=final_df.isnull().sum()
print("Missing values in each column:")
print(missing_values)


# In[18]:


#Fill missing values in "FirstName" and "LastName"
final_df['FirstName']=final_df['FirstName'].fillna('xyz')
final_df['LastName']=final_df['LastName'].fillna('xyz')
print("Missing values after filling:")
print(final_df[['FirstName','LastName']].isnull().sum())


# In[19]:


#Filter rows where 'Email' or 'PhoneNumber' is missing
missing_email_phone=final_df[final_df['Email'].isnull() | final_df['PhoneNumber'].isnull()]

print("Rows with missing phone number & email:")
print(missing_email_phone)


# In[20]:


#Drop rows where Churned=0
final_df.dropna(subset=['Email','PhoneNumber'], how='any',inplace=True)

print(final_df[['Email','PhoneNumber']].isnull().sum())


# In[21]:


#Handle JoinDate , Status and Region
missing_values_row=final_df[final_df[['JoinDate','Status','Region']].isnull().any(axis=1)]
print("Rows with missing JoinDate, Status & Region:")
missing_values_row


# In[24]:


#drop rows where both JoinDate, Status, and Region is missing:
final_df.dropna(subset=['JoinDate','Status','Region'], how='any',inplace=True)

print(final_df[['JoinDate','Status','Region']].isnull().sum())


# In[25]:


final_df.shape


# In[26]:


#Handle SubscriptionID, StartDate,EndDate,and PlanType
missing_values_row=final_df[final_df[['SubscriptionID','StartDate','EndDate','PlanType']].isnull().any(axis=1)]
print("Rows with missing SubscriptionID, StartDate,EndDate,PlanType:")
missing_values_row


# In[28]:


#drop rows where SubscriptionID, StartDate,EndDate,and PlanType are missing:
final_df.dropna(subset=['SubscriptionID','StartDate','EndDate','PlanType'], how='all',inplace=True)

print(final_df[['SubscriptionID','StartDate','EndDate','PlanType']].isnull().sum())


# In[29]:


final_df.shape


# In[31]:


#Set "TransactionID" to one less than the minimum existing transaction ID
#Set "TransactionDate" to a date 10 years before the minimum existing transaction date
#Set Amount to 0
#Set Transaction Type to 'No Transaction'

import pandas as pd
from datetime import timedelta

#Ensure TransactionDate is in datetime format,
Transactions_df['TransactionDate']=pd.to_datetime(Transactions_df['TransactionDate'],format='%d-%m-%Y',errors='coerce')

#Find the minimum TransactionDate and TransactionDate
min_transaction_id= Transactions_df['TransactionID'].min()
min_transaction_date=Transactions_df['TransactionDate'].min()

#Define the date 10 years before the minimum transaction Date
ten_years_prior= min_transaction_date - timedelta(days=365*10)

#Fill missing values for customers with no transactions
final_df.loc[final_df['TransactionID'].isnull(),'TransactionID']=min_transaction_id-1
final_df.loc[final_df['TransactionDate'].isnull(),'TransactionDate']=ten_years_prior.strftime('%d=%m-%Y')
final_df.loc[final_df['Amount'].isnull(),'Amount']=0
final_df.loc[final_df['TransactionType'].isnull(),'TransactionType']='No Transaction'

print(final_df[['TransactionID','TransactionDate','Amount','TransactionType']].isnull().sum())


# In[32]:


missing_values=final_df.isnull().sum()
print("Missing values in each column:")
print(missing_values)


# In[33]:


final_df.shape


# In[38]:


import pandas as pd
from datetime import timedelta

#Ensure TransactionDate is in datetime format,
Churn_df['ChurnDate']=pd.to_datetime(Churn_df['ChurnDate'],errors='coerce')

#Find the minimum TransactionDate and TransactionDate
min_churn_id= Churn_df['ChurnID'].min()
min_churn_date=Churn_df['ChurnDate'].min()

#Define the date 10 years before the minimum transaction Date
ten_years_prior= min_churn_date - timedelta(days=365*10)

#Fill missing values for customers with no transactions
final_df.loc[final_df['ChurnID'].isnull(),'ChurnID']=min_churn_id-1
final_df.loc[final_df['ChurnDate'].isnull(),'ChurnDate']=ten_years_prior.strftime('%d=%m-%Y')
final_df.loc[final_df['Reason'].isnull(),'Reason']='Unknown Reason'

print(final_df[['ChurnID','ChurnDate','Reason']].isnull().sum())


# In[39]:


missing_values=final_df.isnull().sum()
print("Missing values in each column:")
print(missing_values)


# In[40]:


final_df.shape


# In[ ]:




