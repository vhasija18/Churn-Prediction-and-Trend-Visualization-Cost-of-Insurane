import tkinter as tk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score as ACS
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

#Initialization of data
def initialize_data():
    data=pd.read_csv(r'C:\Users\hasij\OneDrive\Desktop\health-insurance-data\insurance.csv')
    print(data.head(5))
    gender_d = {'female': 1, 'male':0}
    data['Gender'] = data['Gender'].apply(lambda x: gender_d[x])
    y_n_d = {'yes':1, 'no':0}
    data['Smoker']=data['Smoker'].apply(lambda x :y_n_d[x])
    location_d={'northeast':0,'northwest':1,'southeast':2,'southwest':3}
    data['Region']= data['Region'].apply(lambda x: location_d[x])
    return(data)

#Test and Train data using Polynomial Regression
def test_train(data,a):
    X=data.iloc[:,0:6].values
    Y=data.iloc[:,6].values
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.20,random_state=3)
    poly_features= PolynomialFeatures(degree=5)
    X_train_poly = poly_features.fit_transform(X_train)
    poly_model =LinearRegression()
    poly_model.fit(X_train_poly,Y_train)
    Y_train_predict = poly_model.predict(X_train_poly)
    accuracy = r2_score(Y_train,Y_train_predict)*100
    print("Accuracy is ",accuracy)
    a=poly_features.fit_transform(a.reshape(1,-1))
    coi = poly_model.predict(a)
    return (accuracy,coi[0])

#Some stats abouth data
def data_stats(data):
      number_of_female = data[data['Gender']==1]
      number_of_male   = data[data['Gender']==0]
      number_of_smoker = data[data['Smoker']==1]
      number_of_nonsmoker = data[data['Smoker']==0]
      number_of_female_smoker  = number_of_female[number_of_female['Smoker']==1]
      number_of_female_nsmoker = number_of_female[number_of_female['Smoker']==0]
      number_of_male_smoker    = number_of_male[number_of_male['Smoker']==1]
      number_of_male_nsmoker   = number_of_male[number_of_male['Smoker']==0]
      average_male_charges     = number_of_male.loc[:,'Charges'].mean()
      average_male_smoker_charges = number_of_male_smoker.loc[:,'Charges'].mean()
      average_male_nonsmoker_charges =number_of_male_nsmoker.loc[:,'Charges'].mean()
      average_female_charges      = number_of_female.loc[:,'Charges'].mean()
      average_female_smoker_charges = number_of_female_smoker.loc[:,'Charges'].mean()
      average_female_nsmoker_charges= number_of_female_nsmoker.loc[:,'Charges'].mean()    
      return(len(number_of_female),len(number_of_male),len(number_of_smoker),len(number_of_nonsmoker),
             len(number_of_female_smoker),len(number_of_female_nsmoker),len(number_of_male_smoker),
             len(number_of_male_nsmoker),average_male_charges,average_male_smoker_charges,
             average_male_nonsmoker_charges,average_female_charges,
             average_female_smoker_charges,average_female_nsmoker_charges)

#Function to extract the value from input form
def displaytext(E1,E3,E4,E7,E8,Gender_var,Region_var,Smoker_var):
        a=[]
        age    = E1.get()
        bmi    = E3.get()
        Number_of_children = E4.get()
        Smoker_value = Smoker_var.get()
        Region_value = Region_var.get()
        Gender_value = Gender_var.get()
        print(age,bmi,Number_of_children,Smoker_value,Region_value,Gender_value)
        a.append(int(age))
        a.append(Gender_value)
        a.append(int(bmi))
        a.append(int(Number_of_children))
        a.append(Smoker_value)
        a.append(Region_value)
        a = np.array(a)
        print(a)
        data = initialize_data()
        accuracy ,coi= test_train(data,a)
        E7.insert(5,str(round(accuracy,2))+"%")
        E8.insert(5,"$"+str(round(coi)))

#Function to rest the value of form to null
def  reset(E1,E3,E4,E7,E8,var,Region_var,Smoker_var):
    E1.delete(0,'end')
    E3.delete(0,'end')
    E4.delete(0,'end')
    E7.delete(0,'end')
    E8.delete(0,'end')
    var.set("None")
    Region_var.set("None")
    Smoker_var.set("None")


#Main class to call GUI    
class Maintask(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.geometry("700x350+200+200")
        self.configure(background="#FAF200")
        self.title("Data Analysis")
        self.switch_frame(StartPage)
    
    def switch_frame(self,frame_class):
        new_frame = frame_class(self)
        if(self._frame is not None):
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

#First UI Page : Introduction Page
class StartPage(tk.Frame):
    def __init__(self,master):
        intro = "XYZ Financial is an insurance company in Canada. \nThey want an desktop application for their underwriter which can help him to \ndecide the Cost Of Insurance(COI). Using Polynomial Regression algorithm I build a model\n for him which can estimate COI.\n\n\nLets go ahead and see how algorithm works.  "
        tk.Frame.__init__(self,master)
        self.configure(background="#FAF200")
        self.pack(fill="both",expand=1)
        label1 = tk.Label(self,text=intro,bg="#FAF200", font=("Helvetica", 12))
        label1.place(x=10,y=20)
        button1 = tk.Button(self, text="Next Page",
                  command=lambda: master.switch_frame(PageOne),bg="#55D6FD",activebackground="#FFF08D",font=("Helvetica", 10),width=11)
        button1.place(x=290,y=200)

#2nd UI Page : User Input Form
class PageOne(tk.Frame):
  
    def __init__(self, master):
        var = tk.IntVar()
        Region_var = tk.IntVar()
        Smoker_var = tk.IntVar()
        tk.Frame.__init__(self, master)
        self.configure(background="#FAF200")
        self.pack(fill="both",expand=1)
        label1 = tk.Label(self, text="Age",width=15,font=("Helvetica", 10))
        label2 = tk.Label(self, text="Gender (M/F)",width=15,font=("Helvetica", 10))
        label3 = tk.Label(self, text="BMI",width=15,font=("Helvetica", 10))
        label4 = tk.Label(self, text="Number of children",width=15,font=("Helvetica", 10))
        label5 = tk.Label(self, text="Smoker (Y/N)",width=15,font=("Helvetica", 10))
        label6 = tk.Label(self, text="Region",width=15,font=("Helvetica", 10))
        label7 = tk.Label(self, text="Accuracy",width="15",font=("Helvetica", 10))
        label8 = tk.Label(self, text="Estimated COI",width="15",font=("Helvetica", 10))
        label1.place(x=100,y=20)
        label2.place(x=100,y=45)
        label3.place(x=100,y=70)
        label4.place(x=100,y=95)
        label5.place(x=100,y=120)
        label6.place(x=100,y=145)
        label7.place(x=100,y=170)
        label8.place(x=100,y=195)
        e1 = tk.Entry(self,width=40,font=("Helvetica", 10))
        e3 = tk.Entry(self,width=40,font=("Helvetica", 10))
        e4 = tk.Entry(self,width=40,font=("Helvetica", 10))
        #e5 = tk.Entry(self,width=40)
        e7 = tk.Entry(self,width=40,font=("Helvetica", 10))
        e8 = tk.Entry(self,width=40,font=("Helvetica", 10))
        e1.place(x=230,y=20)
        e3.place(x=230,y=70)
        e4.place(x=230,y=95)
        #e5.place(x=230,y=120)  
        e7.place(x=230,y=170)
        e8.place(x=230,y=195)
        def GetValue():
            print(var.get())
        def Get_Region():
            print(Region_var.get())
        var.set("None")
        Region_var.set("None")
        Smoker_var.set("None")
        R1 = tk.Radiobutton(self,text= "Female",variable = var, value = 1,command = GetValue,width=10,bg="#FAF200",font=("Helvetica", 10))
        R1.place(x=230,y=45)
        R2 = tk.Radiobutton(self,text="Male",variable = var,value=0,command= GetValue,width=10,bg="#FAF200",font=("Helvetica", 10))
        R2.place(x=330,y=45)
        R3 = tk.Radiobutton(self,text="NE",variable = Region_var,value=0,command= Get_Region,width=7,bg="#FAF200",font=("Helvetica", 10))
        R3.place(x=230,y=145)
        R4 = tk.Radiobutton(self,text="NW",variable = Region_var,value=1,command= Get_Region,width=6,bg="#FAF200",font=("Helvetica", 10))
        R4.place(x=300,y=145)
        R5 = tk.Radiobutton(self,text="SE",variable = Region_var,value=2,command= Get_Region,width=7,bg="#FAF200",font=("Helvetica", 10))
        R5.place(x=370,y=145)
        R6 = tk.Radiobutton(self,text="SW",variable = Region_var,value=3,command= Get_Region,width=7,bg="#FAF200",font=("Helvetica", 10))
        R6.place(x=440,y=145)
        R7 = tk.Radiobutton(self,text= "Smoker",variable = Smoker_var, value = 1,command = GetValue,width=15,bg="#FAF200",font=("Helvetica", 10))
        R7.place(x=230,y=120)
        R8 = tk.Radiobutton(self,text="Non Smoker",variable = Smoker_var,value=0,command= GetValue,width=20,bg="#FAF200",font=("Helvetica", 10))
        R8.place(x=350,y=120)
        
        
        submit_button = tk.Button(self, text="Submit",command = lambda : displaytext(e1,e3,e4,e7,e8,var,Region_var,Smoker_var),bg="#55D6FD",activebackground="#FFF08D",font=("Helvetica", 10))
        submit_button.place(x=230,y=250)
        
        reset_button = tk.Button(self,text="Rest Values", command = lambda: reset(e1,e3,e4,e7,e8,var,Region_var,Smoker_var),bg="#55D6FD",activebackground="#FFF08D",font=("Helvetica", 10))
        reset_button.place(x=298,y=250)
                
        next_button = tk.Button(self, text="Next Page",command=lambda: master.switch_frame(PageSecond),bg="#55D6FD",activebackground="#FFF08D",font=("Helvetica", 10))
        next_button.place(x=400,y=250)
        
#3rd Page: Stats about the data                
class PageSecond(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        self.configure(background="#FAF200")
        self.pack(fill="both",expand=1)
        data = initialize_data()
        number_of_female,number_of_male,number_of_smoker,number_of_nonsmoker,number_of_female_smoker,_,_,_,_,_,_,_,_,_ = data_stats(data)
        label_page_one =tk.Label(self, text="Some Stats About the Data",bg="#FAF200",font=("Helvetica",11))
        label_page_one.place(x=250,y=10)
        Q1= tk.Label(self,text="Q. How many female we have consider in this data?",bg="#FAF200",font=("Helvetica", 11))
        Q1.place(x=20,y=40)
        A1= tk.Label(self,text="Tim, there are " + str(number_of_female) +" females.",bg="#FAF200",font=("Helvetica", 11),fg="#027596")
        A1.place(x=20,y=60)
        Q2 = tk.Label(self,text= "Q. Jack, What about the number of males we are looking at?",font=("Helvetica", 11),bg="#FAF200")
        Q2.place(x=20,y=90)
        A2 = tk.Label(self,text = "There are "+ str(number_of_male) + " males, Ray!",bg="#FAF200",font=("Helvetica", 11),fg="#027596")
        A2.place(x=20,y=110)
        Q3 = tk.Label(self,text= "Q. Jack, What is the percentage of Smoker?",font=("Helvetica", 11),bg="#FAF200")
        Q3.place(x=20,y=140)
        smoker_percent = round((number_of_smoker/1339)*100,2)
        A3 = tk.Label(self,text = "There are "+ str(smoker_percent) + " percent of smokers. That is " + str(number_of_smoker) + " smokers out of 1339.",bg="#FAF200",font=("Helvetica", 11),fg="#027596")
        A3.place(x=20,y=160)
        Q4 = tk.Label(self,text= "Q. Are we considering female smokers?",font=("Helvetica", 11),bg="#FAF200")
        Q4.place(x=20,y=190)
        A4 = tk.Label(self,text = "Yes ofcourse we did, there are " + str(number_of_female_smoker)+ " number of female smoker.",bg="#FAF200",font=("Helvetica", 11),fg="#027596")
        A4.place(x=20,y=210)
        button_page_one = tk.Button(self, text="Prev Page",command=lambda: master.switch_frame(PageOne),bg="#55D6FD",activebackground="#FFF08D",font=("Helvetica", 11))
        button_page_one.place(x=220,y=280)
        button_page_third = tk.Button(self,command=lambda: master.switch_frame(PageThird), text="Next Page",bg="#55D6FD",activebackground="#FFF08D",font=("Helvetica", 11))
        button_page_third.place(x=350,y=280)

#4th Page: Stats about the data
class PageThird(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        self.configure(background="#FAF200")
        self.pack(fill="both",expand=1)
        data = initialize_data()
        _,_,_,_,_,_,number_of_male_smoker,number_of_male_nsmoker,average_male_charges,average_male_smoker_charges,average_male_nsmoker_charges,_,_,_ = data_stats(data)
        label_page_one =tk.Label(self, text="Some Stats About the Data",bg="#FAF200",font=("Helvetica",11))
        label_page_one.place(x=250,y=10)
        Q1= tk.Label(self,text="Q. What is the average charge for male.",bg="#FAF200",font=("Helvetica", 11))
        Q1.place(x=20,y=40)
        A1= tk.Label(self,text="Bob, average cost of insurance for male is "+ str(round(average_male_charges,2)),bg="#FAF200",font=("Helvetica", 11),fg="#027596")
        A1.place(x=20,y=60)
        Q2 = tk.Label(self,text= "Q. Steph, what about the average cost of insurance for male with smoker status?",font=("Helvetica", 11),bg="#FAF200")
        Q2.place(x=20,y=90)
        A2 = tk.Label(self,text = "Average cost of insurance for "+str(number_of_male_smoker) + " male smoker is "+ str(round(average_male_smoker_charges,2))+ ", Ray!",bg="#FAF200",font=("Helvetica", 11),fg="#027596")
        A2.place(x=20,y=110)
        Q3 = tk.Label(self,text= "Q. What is the average COI for non smoker males?",font=("Helvetica", 11),bg="#FAF200")
        Q3.place(x=20,y=140)
        A3 = tk.Label(self,text = "Average COI for non smoker male is "+ str(round(average_male_nsmoker_charges,2))+ "." ,bg="#FAF200",font=("Helvetica", 11),fg="#027596")
        A3.place(x=20,y=160)
        button_page_second = tk.Button(self, text="Prev Page",command=lambda: master.switch_frame(PageSecond),bg="#55D6FD",activebackground="#FFF08D",font=("Helvetica", 11))
        button_page_second.place(x=220,y=230)
        button_page_fourth = tk.Button(self,command=lambda: master.switch_frame(PageFourth), text="Next Page",bg="#55D6FD",activebackground="#FFF08D",font=("Helvetica", 11))
        button_page_fourth.place(x=340,y=230)

#5th Page: Stats about the data
class PageFourth(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        self.configure(background="#FAF200")
        self.pack(fill="both",expand=1)
        data = initialize_data()
        _,_,_,_,_,_,_,_,_,_,_,average_female_charges,average_female_smoker_charges,average_female_nsmoker_charges = data_stats(data)
        label_page_one =tk.Label(self, text="Some Stats About the Data",bg="#FAF200",font=("Helvetica",11))
        label_page_one.place(x=250,y=10)
        Q1= tk.Label(self,text="Q. What is the average charge for female.",bg="#FAF200",font=("Helvetica", 11))
        Q1.place(x=20,y=40)
        A1= tk.Label(self,text="Bob, average cost of insurance for female is "+ str(round(average_female_charges,2)),bg="#FAF200",font=("Helvetica", 11),fg="#027596")
        A1.place(x=20,y=60)
        Q2 = tk.Label(self,text= "Q. Steph, what about the average cost of insurance for female with smoker status?",font=("Helvetica", 11),bg="#FAF200")
        Q2.place(x=20,y=90)
        A2 = tk.Label(self,text = "Average cost of insurance for female smoker is "+ str(round(average_female_smoker_charges,2))+ ", Ray!",bg="#FAF200",font=("Helvetica", 11),fg="#027596")
        A2.place(x=20,y=110)
        Q3 = tk.Label(self,text= "Q. What is the average COI for non smoker females?",font=("Helvetica", 11),bg="#FAF200")
        Q3.place(x=20,y=140)
        A3 = tk.Label(self,text = "Average COI for non smoker female is "+ str(round(average_female_nsmoker_charges,2))+ "." ,bg="#FAF200",font=("Helvetica", 11),fg="#027596")
        A3.place(x=20,y=160)
        button_page_third = tk.Button(self, text="Prev Page",command=lambda: master.switch_frame(PageThird),bg="#55D6FD",activebackground="#FFF08D",font=("Helvetica", 11))
        button_page_third.place(x=200,y=220)
        button_quit = tk.Button(self,command= self.destroy,text="Quit",bg="#55D6FD",activebackground="#FFF08D",font=("Helvetica", 11),width=8)
        button_quit.place(x=300,y=220)
        
if __name__ == "__main__":
    app = Maintask()
    app.mainloop()

