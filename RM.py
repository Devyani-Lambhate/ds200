


import os
import json
from matplotlib import pyplot as plt
import numpy as np

path='indore.json'


with open(path, "r") as read_file:
	dataset = json.load(read_file)
		
n=len(dataset)
#print(dataset)
data=dataset['data']
data=np.array(data)
#print(data[:,7])


age= data[:,4].astype(np.float)

data_male = data[data[:,5] == 'Male']
age_male=data_male[:,4].astype(np.float)
data_female = data[data[:,5] == 'Female']
age_female=data_female[:,4].astype(np.float)

#print(age_male)

sex=data[:,5]
#print(sex)

################### bar plot #####################
#y = death[:,4].astype(np.float)
fig,ax = plt.subplots(1,1)
ax.hist([age_male,age_female], bins = [0,10,20,30,40,50,60,70,80,90,100],rwidth=0.85,stacked=True, label=['male','female'])
ax.set_title("Number of Covid 19 cases in Indore v/s age in Indore city \n from 2nd April to 29th June, 2020")
ax.legend(prop={'size': 10})

ax.set_xticks([0,10,20,30,40,50,60,70,80,90,100])
ax.set_xlabel('age')
ax.set_ylabel('no. of patients')
plt.grid(axis='y', alpha=0.5)
plt.savefig('bar plot.png')




############### box plot ######################

fig,ax = plt.subplots(figsize =(10, 7)) 
ax.set_title("Age distribution of Covid positive patients in indore")
# Creating plot 
ax.boxplot([age,age_male,age_female]) 
ax.set_xticklabels(['all','male ','female '])
ax.set_ylabel('age')
# show plot 
plt.grid(axis='y', alpha=0.5)
plt.savefig('box plot.png') 



############Scatter plot ######################

fig,ax=plt.subplots(1,1)
death = data[data[:,8] == 'Death']
y = death[:,4].astype(np.float)

age,death_count=np.unique(y,return_counts=True)
print('!!!!!!!!!!!',age,death_count)
#print(death_count)
age_t,positive_count=np.unique(data[:,4].astype(np.float),return_counts=True)
print('@@@@@@@@@@@@',age_t,positive_count)
#print(positive_count)
age= age.astype(np.int)
age_t= age_t.astype(np.int)
fatality_rate=[]

for i in age_t:
	if(i in age):
		x=np.where(age == i)
		y=np.where(age_t==i)
		fatality_rate.append(death_count[x[0]]/positive_count[y[0]])

	#else:
		#fatality_rate.append(0)

#print(count.shape,death_count.shape)
ax.scatter(age, fatality_rate , c ="blue") 
plt.grid(axis='y', alpha=0.5)
plt.grid(axis='x', alpha=0.5)
ax.set_xlabel('age')
ax.set_ylabel('fatality rate')
ax.set_title("fatality rate of Covid Positive patients v/s age in Indore city")
# To show the plot 
plt.savefig('scatter.png') 



