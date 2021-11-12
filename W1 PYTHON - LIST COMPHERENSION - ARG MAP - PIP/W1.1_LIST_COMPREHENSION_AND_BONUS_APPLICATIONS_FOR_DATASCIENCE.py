
##******** W1.1 -  List Comprehension AND Bonus Exercises FOR DATA SCIENCE  ##*********

# Task 1: Load the car_crashes dataset.
# Capitalize the names of the numeric variables in the car_crashes data and add NUM to the beginning.
#############################################

# Try to get the following output by reading the data set from the beginning.

# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:

# ['NUM_TOTAL',
#  'NUM_SPEEDING',
#  'NUM_ALCOHOL',
#  'NUM_NOT_DISTRACTED',
#  'NUM_NO_PREVIOUS',
#  'NUM_INS_PREMIUM',
#  'NUM_INS_LOSSES',
#  'ABBREV']

# Hints:
# Non-numeric names should also capitalize.
# Must be done with a single list comprehension structure.

import seaborn as sns

df=sns.load_dataset("car_crashes")
df.head()
df.columns

new_cols= [ "NUM_"+col.upper() if df[col].dtype in [int,float] else col.upper() for col in df.columns]
new_cols

#############################################
# Task 2: Type "FLAG" AFTER the names of variables that DOES NOT contain "no" in their name.
# #############################################
#
# # All variable names must be uppercase.
# # A single list should be made with comp.
#
# # Expected output:
#
# # ['TOTAL_FLAG',
# # 'SPEEDING_FLAG',
# # 'ALCOHOL_FLAG',
# # 'NOT_DISTRACTED',
# # 'NO_PREVIOUS',
# # 'INS_PREMIUM_FLAG',
# # 'INS_LOSSES_FLAG',
# # 'ABBREV_FLAG']

import seaborn as sns

df=sns.load_dataset("car_crashes")
df.head()
df.columns

new_columns = [cols.upper()+"_FLAG" if "no" not in cols else cols.upper() for cols in df.columns ]
new_columns

#############################################
# Task 3: Create a new df by selecting the names of the variables that are DIFFERENT from the variable names given below.
#############################################

# og_list = ["abbrev", "no_previous"]


# First, create a new list named new_cols using list comprehension according to the list above.
# Then create a new df by selecting these variables with df["new_cols"] and name it as new_df.

# Expected output:
# new_df.head()
#
#    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# 0 18.800     7.332    5.640          18.048      784.550     145.080
# 1 18.100     7.421    4.525          16.290     1053.480     133.930
# 2 18.600     6.510    5.208          15.624      899.470     110.350
# 3 22.400     4.032    5.824          21.056      827.340     142.390
# 4 12.000     4.200    3.360          10.920      878.410     165.630

import seaborn as sns

df=sns.load_dataset("car_crashes")
df.head()
df.columns
og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
df=df[new_cols]
df

# BONUS PART (DICTIONARY COMPREHENSION) #
#############################################
# Task 4: : Create a dictionary as follows. Take only numeratical columns
#############################################
#Hint : Create a dynamically special Dictionary which have got a key as string and value as a List

# Expected output:

# {'total': ['mean', 'min', 'max', 'var'],
# 'speeding': ['mean', 'min', 'max', 'var'],
# 'alcohol': ['mean', 'min', 'max', 'var'],
# 'not_distracted': ['mean', 'min', 'max', 'var'],
# 'no_previous': ['mean', 'min', 'max', 'var'],
# 'ins_premium': ['mean', 'min', 'max', 'var'],
# 'ins_losses': ['mean', 'min', 'max', 'var']}

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

agg_list = ['mean', 'min', 'max', 'sum']
num_cols = [col for col in df.columns if df[col].dtype in [int,float]]
new_dict = {col:agg_list  for col in num_cols }
df.groupby("abbrev").agg(new_dict)

#############################################################
# Task 4.1 : For task 4 Use aggregation function            #
# with a new_dict and group dataframe df by "abbrev" column #
#############################################################

df.groupby("abbrev").agg(new_dict)

##################################################
# Task 5 Create a dictionary as follows: #
##################################################
#Hint : Create a dynamically special Dictionary which has got a key as string and value as a List

# before:

# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],

# after:

# {'total': ['total_mean', 'total_min', 'total_max', 'total_var'],
# 'speeding': ['speeding_mean', 'speeding_min', 'speeding_max', 'speeding_var'],
# 'alcohol': ['alcohol_mean', 'alcohol_min', 'alcohol_max', 'alcohol_var']

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

agg_list = ['mean', 'min', 'max', 'sum']
num_cols = [col for col in df.columns if df[col].dtype in [int,float]]
new_dict = {col:agg_list  for col in num_cols }

new_dict2 = {col:[str(col)+"_"+i for i in agg_list ] for col in new_dict}
new_dict2

######################################################
# TASK 6 :  We want to create a dictionary as follows:
######################################################

# PURPOSE: Let's want to assign the first element of a list as key and the other set of elements as value.

# before
# total speeding alcohol not_distracted no_previous
# 0 18.8 7.332 5.640 18.048 15.040
# 1 18.1 7.421 4,525 16,290 17.014
# 2 18.6 6,510 5,208 15,624 17,856
# 3 22.4 4.032 5.824 21.056 21.280
# 4 12.0 4.200 3.360 10.920 10.680


# after:
# {18.8: [7, 5, 18, 15],
# 18.1: [7, 4, 16, 17],
# 18.6: [6, 5, 15, 17],
# 22.4: [4, 5, 21, 21],
# 12.0: [4, 3, 10, 10]}

import seaborn as sns

df = sns.load_dataset("car_crashes")
num_cols = [col for col in df.columns if df[col].dtype in [int,float]]

new_df=df[num_cols]

new_dict3 = {new_df.values[s,:][0]:[ int(i) for i in new_df.values[s,:][1:]] for s in range(len(new_df))}
new_dict3

