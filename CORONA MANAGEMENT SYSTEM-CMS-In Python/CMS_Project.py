import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

pd.set_option('display.max_columns',None)
pd.set_option('display.width', 5000)

line1="----------------------------------------------------------------------------- \n"
line2="\n----------------------------------------------------------------------------- \n"
line3=("-----------------------------------------------------------------------------")
line4="\n-----------------------------------------------------------------------------"

def menu():
    print("\n \n \t \t \t \t  ###################################### \n")
    print("\t \t \t \t     CORONA MANAGEMENT SYSTEM (C.M.S) \n")
    print("\t \t \t \t  ###################################### \n")
    print(line1)
    print("\t 1.Read Data From The CSV Files \n")
    print("\t 2.Data Visualization \n")
    print("\t 3.Data Sorting And Manipulation \n")
    print("\t 4.Update Data \n")
    print(line3)

menu()

def Error():
    print("\n \n \t \t \t \t INVALID  INPUT ! ")
    print(line2)
    input("\t Press Enter to Re-execute:")
    print(line2)
    
def ReadData():
    print(line2)
    print("\t --> Read The Following CSV Files: \n")
    print("\t 1. 'Cases' Data \n")
    print("\t 2. 'Resources' Data \n")
    print(line3)
    opt=input("Input Here: ")
    if opt=="1":
        df=pd.read_csv("Cases.csv")
        print(line2)
        print(df)
    elif opt=="2":
        df=pd.read_csv("Resources.csv")
        print(line2)
        print(df)
    else:
        Error()
        ReadData()

def LineChart():
    print(line2)
    df1=pd.read_csv("Cases.csv")
    df2=pd.read_csv("Resources.csv")
    clmn1=df1.columns[1:]
    clmn2=df2.columns[1:]
    print(" --> FIELDS Available : \n")
    for cl1 in clmn1:
        print(cl1)
    for cl2 in clmn2:
        print(cl2)
    print(line4)
    opt=input("Input Field(String):  STATE v/s : ")
    plt.xlabel("State")
    plt.xticks(rotation='vertical')
    if opt in clmn1:
        print(line1)
        plt.plot(df1['State'],df1[opt],color="red")
        plt.ylabel(opt)
        title="State v/s "+opt
        plt.title(title)
        plt.grid()
        plt.show()
    elif opt in clmn2:
        print(line1)
        plt.plot(df2['State'],df2[opt],color="blue")
        plt.ylabel(opt)
        title="State v/s "+opt
        plt.title(title)
        plt.grid()
        plt.show()
    else:
        Error()
        LineChart()

def BarPlot():
    print(line2)
    df1=pd.read_csv("Cases.csv")
    df2=pd.read_csv("Resources.csv")
    clmn1=df1.columns[1:]
    clmn2=df2.columns[1:]
    print(" --> FIELDS Available : \n")
    for cl1 in clmn1:
        print(cl1)
    for cl2 in clmn2:
        print(cl2)
    print(line4)
    opt=input("Input Field(String):  STATE v/s : ")
    plt.xlabel("State")
    plt.xticks(rotation='vertical')
    if opt in clmn1:
        print(line1)
        plt.bar(df1['State'],df1[opt],color="red")
        plt.ylabel(opt)
        title="State v/s "+opt
        plt.title(title)
        plt.grid()
        plt.show()
    elif opt in clmn2:
        print(line1)
        plt.bar(df2['State'],df2[opt],color="red")
        plt.ylabel(opt)
        title="State v/s "+opt
        plt.title(title)
        plt.grid()
        plt.show()
    else:
        Error()
        BarPlot()

def PieChart():
    print(line2)
    df1=pd.read_csv("Cases.csv")
    df2=pd.read_csv("Resources.csv")
    clmn1=df1.columns[1:]
    clmn2=df2.columns[1:]
    print(" --> FIELDS Available : \n")
    for cl1 in clmn1:
        print(cl1)
    for cl2 in clmn2:
        print(cl2)
    print(line4)
    opt=input("Input Field(String):  STATE v/s : ")
    
    if opt in clmn1:
        print(line1)
        plt.pie(df1[opt],autopct="%3d%%")
        title="State v/s "+opt
        plt.title(title)
        plt.legend(df1['State'],title='State',loc='lower left')
        plt.show()
    elif opt in clmn2:
        print(line1)
        plt.pie(df2[opt],autopct="%3d%%")
        title="State v/s "+opt
        plt.title(title)
        plt.legend(df2['State'],title='State',loc='lower left')
        plt.show()
    else:
        Error()
        BarPlot()

def ScatterChart():
    print(line2)
    print("\t --> Select A File For Scatter Chart: \n")
    print("\t 1. 'Cases' Data \n")
    print("\t 2. 'Resources' Data \n")
    print("\t 3.  Both \n")
    print(line3)
    
    df1=pd.read_csv("Cases.csv")
    df2=pd.read_csv("Resources.csv")
    st=df1['State']
    cf=df1['Confirmed']
    rc=df1['Recovered']
    ac=df1['Active']
    dt=df1['Deaths']
    adc=df1['Avg.DailyCases']
    rcr=df1['Recovery(%)']
    hsp=df2['Hospitals']
    vtl=df2['Ventilators']
    bds=df2['Beds']
    icu=df2['ICU_Beds']
    fdr=df2['Funds_Received(in Crores)']

    ax=plt.gca()
    plt.xlabel("State")
    plt.xticks(rotation='vertical')
    opt=input("Input Here: ")
    if opt=='1':
        print(line1)
        ax.scatter(st,cf,color='red',label="State wise Confirmed")
        ax.scatter(st,rc,color='green',label="State wise Recovered")
        ax.scatter(st,ac,color='orange',label="State wise Active")
        ax.scatter(st,dt,color='black',label="State wise Deaths")
        ax.scatter(st,adc,color='brown',label="State wise Avg. Daily Cases")
        ax.scatter(st,rcr,color='cyan',label="State wise Recovery Rate(%)")
        plt.legend()
        plt.title("Scatter Chart For 'Cases' Data")
        plt.grid()
        plt.show()
    elif opt=='2':
        print(line1)
        ax.scatter(st,hsp,color='cyan',label="State wise Hospitals Available")
        ax.scatter(st,vtl,color='green',label="State wise Ventilators Available")
        ax.scatter(st,bds,color='orange',label="State wise Beds Available")
        ax.scatter(st,icu,color='black',label="State wise ICU Beds Available")
        ax.scatter(st,fdr,color='red',label="State wise Funds Received(in Crores)")
        plt.legend()
        plt.title("Scatter Chart For 'Resources' Data")
        plt.grid()
        plt.show()
    elif opt=='3':
        print(line1)
        ax.scatter(st,cf,color='red',label="State wise Confirmed")
        ax.scatter(st,rc,color='green',label="State wise Recovered")
        ax.scatter(st,ac,color='orange',label="State wise Active")
        ax.scatter(st,dt,color='black',label="State wise Deaths")
        ax.scatter(st,adc,color='brown',label="State wise Avg. Daily Cases")
        ax.scatter(st,rcr,color='cyan',label="State wise Recovery Rate(%)")
        ax.scatter(st,hsp,color='grey',label="State wise Hospitals Available")
        ax.scatter(st,vtl,color='violet',label="State wise Ventilators Available")
        ax.scatter(st,bds,color='tan',label="State wise Beds Available")
        ax.scatter(st,icu,color='lawngreen',label="State wise ICU Beds Available")
        ax.scatter(st,fdr,color='deepskyblue',label="State wise Funds Received(in Crores)")
        plt.legend()
        plt.title("Complete Scatter Chart")
        plt.grid()
        plt.show()
    else:
        Error()
        ScatterChart()

def CompareTwoStates():
    print(line2)
    print(" --> STATES Available \n")
    df1=pd.read_csv("Cases.csv")
    df2=pd.read_csv("Resources.csv")
    st=df1['State'].to_string(index=False)
    print(st)
    print(line2)
    st1=input("Input State 1(String): ")
    st2=input("Input State 2(String): ")
    if (st1 in st) and (st2 in st) and (st1 != st2) and st1 !='' and st2 !='' :
        print(line2)
        clmn1=df1.columns[1:]
        clmn2=df2.columns[1:]
        print(" --> FIELDS Available : \n")
        for cl1 in clmn1:
            print(cl1)
        for cl2 in clmn2:
            print(cl2)
        print(line4)
        field=input("Input A Field(String): ")
        if field in clmn1:
            print(line1)
            plt.bar([st1],[df1.loc[df1['State'] == st1, field].iloc[0]])
            plt.bar([st2],[df1.loc[df1['State'] == st2, field].iloc[0]])
            plt.xlabel('State')
            plt.ylabel(field)
            title=st1+' v/s '+st2+' For '+field
            plt.title(title)
            plt.grid()
            plt.show()
        elif field in clmn2:
            print(line1)
            plt.bar([st1],[df2.loc[df2['State'] == st1, field].iloc[0]])
            plt.bar([st2],[df2.loc[df2['State'] == st2, field].iloc[0]])
            plt.xlabel('State')
            plt.ylabel(field)
            title=st1+' v/s '+st2+' For '+field
            plt.title(title)
            plt.grid()
            plt.show()
        else:
            Error()
            CompareTwoStates()
    else:
        Error()
        CompareTwoStates()
    
def DataVisualisation():
    print(line2)
    print("\t --> Select A Type of Visualisation: \n")
    print("\t 1.Line Chart \n")
    print("\t 2.Bar Plot \n")
    print("\t 3.Pie Chart \n")
    print("\t 4.Complete Scatter Chart \n")
    print("\t 5.Compare Two States \n")
    print(line3)
    opt=input("Input Here: ")
    if opt=='1':
        LineChart()
    elif opt=='2':
        BarPlot()
    elif opt=='3':
        PieChart()
    elif opt=='4':
        ScatterChart()
    elif opt=='5':
        CompareTwoStates()
    else:
        Error()
        DataVisualisation()
    
def DataManipulation():
    print(line2)
    print("\t --> Select an Option: \n")
    print("\t 1.Sort Data \n")
    print("\t 2.Read A Specific Column \n")
    print("\t 3.Read Specific Top and Bottom Records \n")
    print("\t 4.Read a Specific Cell Value \n")
    print("\t 5.Get Sum of Data for a Specific Column\n")
    print(line1)
    df1=pd.read_csv("Cases.csv",index_col=0)
    df2=pd.read_csv("Resources.csv",index_col=0)
    clmn1=df1.columns
    clmn2=df2.columns
    opt=input("Input Here: ")
    
    if opt=='1':
        print(line2)
        print(" --> Select A Field To Sort : \n")
        for cl1 in clmn1:
            print(cl1)
        for cl2 in clmn2:
            print(cl2)
        print(line4)
        field=input("Input Field(String): ")
        if field in clmn1:
            print(line2)
            print("\t --> Select A Sorting Order : \n")
            print("\t 1.Ascending Order")
            print("\t 2.Descending Order")
            print(line4)
            odr=input("Input Here: ")
            if odr=='1':
                print(line1)
                df1.sort_values([field],inplace=True,ascending=True)
                print(df1)
            elif odr=='2':
                df1.sort_values([field],inplace=True,ascending=False)
                print(df1)
            else:
                Error()
                DataManipulation()

        elif field in clmn2:
            print(line2)
            print("\t --> Select A Sorting Order : \n")
            print("\t 1.Ascending Order")
            print("\t 2.Descending Order")
            print(line4)
            odr=input("Input Here: ")
            if odr=='1':
                print(line1)
                df2.sort_values([field],inplace=True,ascending=True)
                print(df2)
            elif odr=='2':
                df2.sort_values([field],inplace=True,ascending=False)
                print(df2)
            else:
                Error()
                DataManipulation()
        else:
            Error()
            DataManipulation()
            
    elif opt=='2':
        print(line2)
        print(" --> Select A Specific Column : \n")
        for cl1 in clmn1:
            print(cl1)
        for cl2 in clmn2:
            print(cl2)
        print(line4)
        field=input("Input Column(String): ")
        if field in clmn1:
            print(line2)
            df3=pd.read_csv("Cases.csv",usecols=['State',field])
            print(df3)
        elif field in clmn2:
            print(line2)
            df4=pd.read_csv("Resources.csv",usecols=['State',field])
            print(df4)
        else:
            Error()
            DataManipulation()
            
    elif opt=='3':
        print(line2)
        print("\t --> Select A CSV File : \n")
        print("\t 1. 'Cases' File \n")
        print("\t 2. 'Resources' File")
        print(line4)
        df1=pd.read_csv("Cases.csv",index_col=0)
        df2=pd.read_csv("Resources.csv",index_col=0)
        csv=input("Input Here: ")
        if csv=='1':
            print(line1)
            top=input("\t Input Number of Records To Display From Top: ")
            bottom=input("\t Input Number of Records To Display From Bottom: ")
            if top.isdigit() and bottom.isdigit():
                print(line2)
                print(" --> First",top,"Records : \n")
                print(df1.head(int(top)))
                print('\n')
                print(" --> Last",bottom,"Records : \n")
                print(df1.tail(int(bottom)))
                print('\n')
            else:
                Error()
                DataManipulation()
                
        elif csv=='2':
            print(line1)
            top=input("\t Input Number of Records To Display From Top: ")
            bottom=input("\t Input Number of Records To Display From Bottom: ")
            if top.isdigit() and bottom.isdigit():
                print(line2)
                print(" --> First",top,"Records : \n")
                print(df2.head(int(top)))
                print('\n')
                print(" --> Last",bottom,"Records : \n")
                print(df2.tail(int(bottom)))
                print('\n')
            else:
                Error()
                DataManipulation()
        else:
            Error()
            DataManipulation()
            
    elif opt=='4':
        print(line2)
        print(" --> STATES Available \n")
        df1=pd.read_csv("Cases.csv",index_col=0)
        df2=pd.read_csv("Resources.csv",index_col=0)
        df=pd.read_csv("Cases.csv")
        st=df['State'].to_string(index=False)
        print(st)
        print(line4)
        st1=input("Input A State(String): ")
        if (st1 in st) and st1 !='':
            print(line2)
            print(" --> FIELDS Available \n")
            for cl1 in clmn1:
                print(cl1)
            for cl2 in clmn2:
                print(cl2)
            print(line4)
            field=input("Input A Field(String): ")
            if field in clmn1:
                print(line2)
                print("\t --> ",field,"For",st1,"is:",df1.loc[st1,field])
                print(line2)
            elif field in clmn2:
                print(line2)
                print("\t --> ",field,"For",st1,"is:",df2.loc[st1,field])
                print(line2)
            else:
                Error()
                DataManipulation()
        else:
            Error()
            DataManipulation()
            
    elif opt=='5':
        print(line2)
        print(" --> FIELDS Available : \n")
        for cl1 in df1.columns[1:-1]:
            print(cl1)
        for cl2 in clmn2:
            print(cl2)
        print(line4)
        field=input("Input A Field(String): ")
        if field in df1.columns[1:-1]:
            print(line2)
            total=df1[field].sum()
            print("\t --> Total Sum For",field,"Is:",total)
            print(line2)
        elif field in clmn2:
            print(line2)
            total=df2[field].sum()
            print("\t --> Total Sum For",field,"Is:",total)
            print(line2)
        else:
            Error()
            DataManipulation()
    else:
        Error()
        DataManipulation()

def UpdateData():
    print(line2)
    print(" --> STATES Available \n")
    df=pd.read_csv("Cases.csv")
    df1=pd.read_csv("Cases.csv",index_col=0)
    df2=pd.read_csv("Resources.csv",index_col=0)
    st=df['State'].to_string(index=False)
    print(st)
    print(line4)
    st1=input("Input A State Here(String): ")
    if (st1 in st) and st1 !='' :
        print(line2)
        print(" --> Enter A Field To Update : \n")
        clmn1=df1.columns[1:]
        clmn2=df2.columns[1:]
        for cl1 in clmn1:
            print(cl1)
        for cl2 in clmn2:
            print(cl2)
        print(line4)
        field=input("Input Here(String): ")
        if field in clmn1:
            print(line2)
            old=df1.loc[st1,field]
            print("\t Current Value:",old)
            print("\n")
            new=input("Input A New Value: ")
            if new.isdigit() and old != int(new):
                print(line2)
                df1.loc[st1,field]=int(new)
                df1.to_csv("Cases.csv")
                print("\t \t Data Updated Successfully ! \n")
                
            elif type(eval(new))==float and old != float(new):
                print(line2)
                df1.loc[st1,field]=float(new)
                df1.to_csv("Cases.csv")
                print("\t \t Data Updated Successfully ! \n")
            else:
                Error()
                UpdateData()
        elif field in clmn2:
            print(line2)
            old=df2.loc[st1,field]
            print("\t Current Value:",old)
            print("\n")
            new=input("Input A New Value: ")
            if new.isdigit() and old != int(new):
                print(line2)
                df2.loc[st1,field]=int(new)
                df2.to_csv("Resources.csv")
                print("\t \t Data Updated Successfully ! \n")
            else:
                Error()
                UpdateData()
        else:
            Error()
            UpdateData()
    else:
        Error()
        UpdateData()

def MainOption():
    opt=input("Input Here: ")
    if opt=='1':
        ReadData()
    elif opt=='2':
        DataVisualisation()
    elif opt=='3':
        DataManipulation()
    elif opt=='4':
        UpdateData()
    else:
        Error()
        menu()
        MainOption()

MainOption()
    
