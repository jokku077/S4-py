import matplotlib.pyplot as plt
df = {'Africa':11.7, 'Asia':10.4, 'Europe':1.9, 'North America':9.4, 'Oceania':3.3, 'South America':6.9, 'Soviet Union':7.9}
cont=['Africa' , 'Asia' , 'Europe' , 'N America ','Oceania','S America ','Soviet Union']
area =[11.7,10.4,1.9,9.4,3.3,6.9,7.9]
c=['Area']
plt.bar(cont , area,color='green',width=.5)
plt.title('Continental Areas',color= 'red')
plt.xlabel('Continents')
plt.ylabel('Area (millions of square kilometers)')
plt.legend(c)
plt.show()
