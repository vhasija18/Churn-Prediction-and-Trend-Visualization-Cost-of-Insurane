import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import seaborn as sns

#Pie Chart representing the percentage of  male and female
def pie(data):
    f,ax= plt.subplots(figsize=(15,5))
    df=data.groupby(['Gender'])["Gender"].count()
    gender_labels= ['Female','Male']
    colors =["#1f77b4", "#ff7f0e"]
    explode = (0.1,0)
    plt.title("Percentage of Male and Female", color="#0FFC23", fontsize = 16)
    plt.pie(df,labels = gender_labels, explode=explode,colors=colors,autopct='%1.1f%%', shadow=True, startangle=140,textprops={'fontsize': 15})
    plt.savefig(r"D:\Niagra PIcs\Pie_chart.png", bbox_inches='tight')
    plt.show()
    
#Bar Graph representing the Number of Policy Holder in each Region
def bar_graph(data):
    fg,ax = plt.subplots(figsize=(15,7))
    index = np.arange(len(data.groupby(['Region'])))
    location_labels=['Northeast','NorthWest','Southeast', 'Southwest']
    population = data.groupby(['Region'])['Region'].count()
    barlist = plt.bar(index,population)
    barlist[0].set_color('#FFB433')
    barlist[2].set_color('#46D531')
    barlist[3].set_color('#39D1C2') 
    ax.set_axisbelow(True)
    ax.yaxis.grid(linestyle = '-' , linewidth = '0.5', color='red')
    plt.xlabel('Region', fontsize =25,color="#3e8e41")
    plt.ylabel('Number of people', fontsize =25,color="#3e8e41")
    plt.xticks(index,location_labels,fontsize=20,rotation=30)
    plt.title("Region wise Policy Holders",color="#0FFC23",y=1.1, fontsize = 30)
    plt.savefig(r"D:\Niagra PIcs\Bar_graph_1.png", bbox_inches='tight')
    plt.show()

#Cost of Insurance of Smoker and Non Smoker based on their ages 
def scatter_plot(data):
    f = plt.figure(figsize=(25,15))
    ax = f.add_subplot(121)
    g = sns.scatterplot(x='Age',y='Charges',data=data,palette='magma',hue='Smoker',ax=ax)
    g.set_xlabel("Age",labelpad=25,color="#3e8e41",fontsize=25)
    g.set_ylabel("Charges",labelpad=25,color="#3e8e41",fontsize=25)             
    plt.title('Distribution of Charges vs age ',color= "#0FFC23",y=1.02, fontsize = 30)
    plt.savefig(r"D:\Niagra PIcs\Scatter_plot.png", bbox_inches='tight')
    plt.show()

#Male and Female policy holders in each region
def dual_bar_graph(data):
    f = plt.figure(figsize=(20,10))
    ax=f.add_subplot(122)
    my_pal = {"female":"#39CED1" , "male":"#C639D1"}
    g = sns.countplot(x='Region', data = data, hue="Gender", ax =ax,palette = my_pal)
    g.set_xlabel("Region", labelpad=25,color="#3e8e41",fontsize=25)
    g.set_ylabel("Policy Holders",labelpad=25,color="#3e8e41",fontsize=25)             
    plt.title('Male and Female Porportion in a Region',color= "#0FFC23",y=1.06, fontsize = 25)
    plt.savefig(r"D:\Niagra PIcs\Dual_bar_graph.png", bbox_inches='tight')
    plt.show()

#Somker and Non Smoker percentage    
def donut(data):
    f,ax= plt.subplots(figsize=(15,5))
    df= data.groupby(["Smoker"])["Smoker"].count()
    labels = ("Non Smoker", "Smoker")
    plt.pie(df,labels=labels,autopct='%1.1f%%',textprops={'fontsize': 20})
    centre = plt.Circle( (0,0), 0.7, color='white')
    p=plt.gcf() 
    p.gca().add_artist(centre)
    plt.axis('equal')
    plt.title('Smoker Percentage',color="#0FFC23",y=1.06, fontsize = 25)
    plt.savefig(r"D:\Niagra PIcs\Donut.png", bbox_inches='tight')
    plt.show()

# Average Cost of Insurance according to BMI
def horizontal_bar(data):
        plt.figure(figsize=(10,6))
        regions = {"low": data[data.BMI<18.5].Charges.mean(),
                    'Normal':data[(data.BMI>18.5)&(data.BMI<24.9)].Charges.mean(),
                    "high": data[data.BMI>24.9].Charges.mean()}
        data_bmi = pd.DataFrame.from_dict(regions,orient='index')
        data_bmi.reset_index(inplace = True)
        data_bmi.columns=['bmi','mean_value']
        g=sns.barplot(y="bmi",x="mean_value", data=data_bmi)
        g.tick_params(labelsize=15)
        g.set_xlabel("Average Cost",fontsize=20,color="#3e8e41", labelpad=25)
        g.set_ylabel("BMI",fontsize=20,color="#3e8e41",labelpad=25)
        for line in range(len(data_bmi)):
            print(data_bmi.bmi[line])
            g.text(data_bmi.mean_value[line],line,round(data_bmi.mean_value[line],2),color="black",ha="center",fontsize=15)
        plt.title("Average charge per BMI group",color="#0FFC23",y=1.06, fontsize = 30)
        plt.savefig(r"D:\Niagra PIcs\Bar_graph_2.png", bbox_inches='tight')
        plt.show()

#Cost of Insurance of Male and Female on the basis of number of children       
def boxplot(data):
    plt.figure(figsize=(20,10))
    g=sns.boxplot(x="Children",y="Charges",hue="Gender",data = data)
    g.set_xlabel("Children",fontsize=25,color="#3e8e41",labelpad=25)
    g.set_ylabel("Charges", fontsize=25,color="#3e8e41",labelpad=25)
    plt.title("Relation between Charges and number of children",color="#0FFC23",y=1.06, fontsize = 30)             
    plt.savefig(r"D:\Niagra PIcs\box_plot.png", bbox_inches='tight')
    plt.show()

#Average Sales per region
def line_graph(data):
    plt.figure(figsize=(14,6))
    regions = {"Northeast" : data[data.Region == "northeast"].Charges.mean(),
               "Northwest" : data[data.Region == "northwest"].Charges.mean(),
               "Southeast" : data[data.Region == "southeast"].Charges.mean(),
               "Southwest" : data[data.Region == "southwest"].Charges.mean()
             }
    data_region = pd.DataFrame.from_dict(regions,orient="index")
    data_region.reset_index(inplace= True)
    data_region.columns=["region","mean_value"]
    g = sns.lineplot(x="region",y="mean_value",data=data_region)
    g.set_xlabel("Regions", fontsize =20,color="#3e8e41",labelpad=25)
    g.set_ylabel("Average Sales", fontsize=20,color="#3e8e41",labelpad=25)
    g.yaxis.grid(linestyle = '-' , linewidth = '0.5', color='red')
    g.tick_params(labelsize=15)
    for line in range(len(data_region)):
         g.text(line,data_region.mean_value[line]+10,round(data_region.mean_value[line],2),color= "black",fontsize=14)
    plt.title("Average Sales per Region",color="#0FFC23",y=1.06, fontsize = 30)
    plt.savefig(r"D:\Niagra PIcs\Line_graph.png", bbox_inches='tight')
    plt.show()
    
#Relation between different features    
def heatmap(data):
    gender = {"female" :1, "male":0 }
    data["Gender"]= data["Gender"].apply(lambda x : gender[x])
    y_n_d = {'yes':1, 'no':0}
    data['Smoker']=data['Smoker'].apply(lambda x :y_n_d[x])
    location_d={'northeast':0,'northwest':1,'southeast':2,'southwest':3}
    data['Region']= data['Region'].apply(lambda x: location_d[x])
    f, ax = plt.subplots(figsize=(10,10))
    corr =data.corr()
    sns.set(font_scale=1.3)
    sns.heatmap(corr,mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(240,10,as_cmap=True), square=True, ax=ax)
    plt.title("Relation between different Elements",color="#0FFC23",y=2.1, fontsize = 20)
    plt.savefig(r"D:\Niagra PIcs\Heat_map.png", bbox_inches='tight')
    plt.show()
    
data=pd.read_csv(r'C:\Users\hasij\OneDrive\Desktop\health-insurance-data\insurance.csv')
pie(data)
bar_graph(data) 
scatter_plot(data)
dual_bar_graph(data)
donut(data)
horizontal_bar(data)
boxplot(data)
line_graph(data)
heatmap(data)