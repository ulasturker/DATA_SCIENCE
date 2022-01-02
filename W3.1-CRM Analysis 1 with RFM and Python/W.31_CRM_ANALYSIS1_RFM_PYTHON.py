

"""
Data Set Information: Dataset named “Online Retail II” includes UK based online store between 01/12/2009 - 09/12/2011 which included the sales. Souvenirs included in the product catalog of this company and these can be considered as promotional items Also known that most of that company’s customers are wholesalers.

#Link to the Data Set: https://archive.ics.uci.edu/ml/datasets/Online+Retail+II

Column/Variable Information: InvoiceNo: Invoice number.

Unique to each transaction, If this code starts with C, means the operation is aborted.

StockCode: Product code. Unique number for each product.

Description: Product name Quantity: Number of products. How many of the products sold on the invoices

InvoiceDate: Invoice date and time.

UnitPrice: Product price (in GBP)

CustomerID: Unique customer number

Country: The name of the country where the customer lives.

Aim identification of customers behaviours towards the business problem and clustering these groups according to the behaviors

Clue:

Those who shows common behaviors will be in the same group. Then feedbacks will be given specifically on the development of techniques for sales and marketing to these groups.

#
PROJECT: Customer Segmentation with RFM
#
An e-commerce company wants to segment its customers and determine marketing strategies according to these segments.
Apply RFM analysis to sheet named "Year 2010-2011" of online_retail_II.xlsx data set.
Where is the dataset? Download the "online_retail_II.xlsx" file at the address below.
https://www.kaggle.com/nathaniel/uci-online-retail-ii-data-set or
https://archive.ics.uci.edu/ml/machine-learning-databases/00502/


"""
#TASK 1: Simulate Exploratary Data Analysis / Data Understanding
# EDA ***********************************************************************************************************

import datetime as dt
import pandas as pd
pd.set_option('display.max_columns',None)
df_=pd.read_excel("online_retail_II.xlsx",sheet_name="Year 2010-2011")
df=df_.copy()
df.head()
df.isnull().sum()
df.info()

# What is the number of unique products :
df["Description"].nunique()

# How many product existed and their quantity :
df["Description"].value_counts().head()

# Which is the most ordered product, show in order?
df.groupby("Description").agg({"Quantity":"sum"}).sort_values("Quantity",ascending=False).head()

# How many invoices have been issued in total?
df["Invoice"].nunique()

# How much money was earn on average per invoice? ,
# (it is necessary to create a new variable by multiplying two variables)
# let's create the df again by removing the returned items

df=df[~df["Invoice"].str.contains("C",na=False)]
df.isnull().sum()
df["TotalPrice"]=df["Price"]*df["Quantity"]
df["TotalPrice"].head()

# What are the most expensive products?
df.sort_values("Price",ascending=False).head()

# How many orders came from which country :

df["Country"].value_counts().head()

# Show each countries earnings :
df.groupby("Country").agg({"TotalPrice": "sum"}).sort_values("TotalPrice", ascending=False).head()

###############################################################
# Data Preparation
###############################################################

df.isnull().sum()
df.dropna(inplace=True)
df.describe([0.01,0.05,0.1,0.25,0.5,0.75,0.90,0.95,0.99]).T

###############################################################
# Calculating RFM Metrics
###############################################################

# Recency, Frequency, Monetary
# Recency: Time from customer's last purchase.
# In other words, it is "the time since the last contact of the customer".
# So to find the recency =
# Today's date-Last purchase (you can see this process below with #the lambda function )
#We find the last time to set references.
# but we add 1 or 2 days more to this date so that those who shop on #that day will not have 0 value. By this way we are obstructing Receny values will become 0.
# here we can see that the last date is 2010–12–09 so as I mentioned #we changed it to 2010–12–11 which is shown as today_date variable

df["InvoiceDate"].max()
today_date=dt.datetime(2011,12,11)
#Lets create the Rfm. We introduced the RFM values in the "Customer #ID" breakdown.We obtained the Frequency value by keeping the number #of pieces with the len() function of the "Invoice" variable.
#We obtained the Monetary value by summing the "TotalPrice" variable #with the sum() function by using lambda functions,
rfm=df.groupby("Customer ID").agg({"InvoiceDate":lambda date : (today_date-date.max()).days,                                 "Invoice":lambda num: len(num),
"TotalPrice": lambda TotalPrice: TotalPrice.sum()})

#We are going to change column names to #"Recency","Frequency","Monetary"

rfm.columns=["Recency","Frequency","Monetary"]
#We should check is there any anomaly in the transactions.If there #is a Transaction Monetary and Frequencey values should be greater #than 0 .
#So In summary We have brought Monetary and Frequency values greater #than 0 in order to prevent the "TotalPrice" variable being empty #even though there is a purchase.
rfm=rfm[(rfm["Monetary"])>0&(rfm["Frequency"]>0)]
rfm

###############################################################
# Calculating RFM Scores
###############################################################

# Recency
rfm["RecencyScore"] = pd.qcut(rfm["Recency"],5,labels=[5,4,3,2,1])
rfm["FrequencyScore"] = pd.qcut(rfm["Frequency"],5,labels=[1,2,3,4,5])
rfm["MonetaryScore"] = pd.qcut(rfm["Monetary"],5,labels=[1,2,3,4,5])
rfm

rfm["RFM_SCORE"]=(rfm["RecencyScore"].astype(str)+rfm["FrequencyScore"].astype(str)+rfm["MonetaryScore"].astype(str))

rfm[rfm["RFM_SCORE"]=="555"].head()

###############################################################
# Naming & Analysing RFM Segments
###############################################################

# RFM Naming
seg_map = {
    r'[1-2][1-2]': 'Hibernating',
    r'[1-2][3-4]': 'At_Risk',
    r'[1-2]5': 'Cant_Loose',
    r'3[1-2]': 'About_to_Sleep',
    r'33': 'Need_Attention',
    r'[3-4][4-5]': 'Loyal_Customers',
    r'41': 'Promising',
    r'51': 'New_Customers',
    r'[4-5][2-3]': 'Potential_Loyalists',
    r'5[4-5]': 'Champions'
}

rfm

rfm['Segment'] = rfm['RecencyScore'].astype(str) + rfm['FrequencyScore'].astype(str)

rfm['Segment'] = rfm['Segment'].replace(seg_map, regex=True)
df[["Customer ID"]].nunique()

rfm[["Segment","Recency","Frequency","Monetary"]].groupby("Segment").agg({["mean","count"]})

import matplotlib.pyplot as plt
segments_counts = rfm['Segment'].value_counts().sort_values(ascending=True)

fig, ax = plt.subplots()

bars = ax.barh(range(len(segments_counts)),
             segments_counts,
             color='silver')
ax.set_frame_on(False)
ax.tick_params(left=False,
              bottom=False,
              labelbottom=False)
ax.set_yticks(range(len(segments_counts)))
ax.set_yticklabels(segments_counts.index)

for i, bar in enumerate(bars):
       value = bar.get_width()
       if segments_counts.index[i] in ['Can\'t loose']:
           bar.set_color('firebrick')
       ax.text(value,
               bar.get_y() + bar.get_height()/2,
               '{:,} ({:}%)'.format(int(value),
                                  int(value*100/segments_counts.sum())),
               va='center',
               ha='left'
              )

plt.show()


rfm[rfm["Segment"] == "Need_Attention"].head()
rfm[rfm["Segment"] == "Need_Attention"].index

############################################
##########################################
# TASK 2: After segmenting the customers,
# lets select 3 segments and divide these 3 segments in terms of both action decisions and the structure of the segments
# (in terms of average RFM values).
##########################################
"""
Let's talk about 6 customer groups according to the tables above.
1- I would recommend more trendy, newly released and relatively expensive products to 'Loyal_Customers' and 'Champions' groups.
I would aim to increase Monetary in these groups. I would take care not to occupy them with unnecessary or small campaigns.
2- 'About_to_Sleep' and' Hibernating groups and have not bought new products from us for a certain time.
but I would try to increase their frequency by suggesting products similar to the ones they bought before
3- Need Attention: I could make a discount, I would reduce my profit for this group. Our product portfolio probably does not fit well to this group, I would recommend any new products to this group, but the prices should be very attractive.
Additionally There are so many people in the "At_Risk" group, I would consider doing a special promotion for this group
"""

############################################
# TASK 3: Select the customer IDs of the "Loyal Customers" class and get the excel output.
##########################################

rfm[rfm["Segment"] == "Loyal_Customers"].head()
rfm[rfm["Segment"] == "Loyal_Customers"].index
new_df = pd.DataFrame()
new_df["Loyal_Customers"] = rfm[rfm["Segment"] == "Loyal_Customers"].index

new_df.to_excel("Loyal_Customers.xlsx")

df
