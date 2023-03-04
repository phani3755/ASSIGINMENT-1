# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 01:08:42 2023

@author: PHANINDRA SAI NAIDU
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 01:23:22 2023

@author: PHANINDRA SAI NAIDU        
"""
#importing libraries

import pandas as pd 
import matplotlib.pyplot as plt


#Defining the Line function
    

def US_Immigration_Statistics():
    '''
    The above function is used to create line plot for us immigration and year

    Returns
    Result shows line plot between year and us immigration
    -------
    None.

    '''
 
    
    #Reading the csv file 1
    
    Is = pd.read_csv('US Immigration Statistics (Ver 1.7.23).csv')
     
    print(Is.describe())
    
    #Conversion from String to integer
    
    Is['Immigrants Obtaining Lawful Permanent Resident Status'] = \
        Is['Immigrants Obtaining Lawful Permanent Resident Status'].\
            str.replace(',','').astype(int)
    Is['Refugee Arrivals'] = Is['Refugee Arrivals'].\
        str.replace(',','').astype(int)
    Is['Noncitizen Apprehensions'] = Is['Noncitizen Apprehensions'].\
        str.replace(',','').astype(int)
    Is['Noncitizen Removals'] = Is['Noncitizen Removals'].\
        str.replace(',','').astype(int)
    Is['Noncitizen Returns'] = Is['Noncitizen Returns'].\
        str.replace(',','').astype(int)
        
    #Plotting data to show in the graph 
    
    plt.plot(Is['Year'], 
        Is['Immigrants Obtaining Lawful Permanent Resident Status'],
        label = 'Lawful Permanent Resident Status',marker = 'o')
    plt.plot(Is['Year'], 
             Is['Refugee Arrivals'],label = 'Refugee Arrivals',marker = '*')
    plt.plot(Is['Year'], 
             Is['Noncitizen Apprehensions'],label = 'Noncitizen Apprehensions')
    plt.plot(Is['Year'], 
             Is['Noncitizen Removals'],label = 'Noncitizen Removals',marker = '.')
    plt.plot(Is['Year'], 
             Is['Noncitizen Returns'],label = 'Noncitizen Returns',marker = '^')
    
    #plotting labels and legend
    
    plt.legend(fontsize = 7 )
    plt.xlabel('Year',fontsize = 10)
    plt.ylabel('US Immigration  Statistics', fontsize = 10)
    plt.title('US Immigration  Statistics 1980-2021')
    
    # used for showing the axis lines
    
    plt.grid()
    
    #used for showing the graph
    
    plt.show()
    
  
    #Defining the bar function
   

def Total_motives(data,col_1,col_2):
    '''

    Parameters
    ----------
    data : TYPE pandas
        DESCRIPTION : 
    col_1 : TYPE  pandas
        DESCRIPTION.
    col_2 : TYPE pandas
        DESCRIPTION.

    Returns
    result shows bar graph
    -------
    None.

    '''
    #Plotting figure and horizontal bar graph
    
    plt.figure()
    plt.barh(data[col_1], data[col_2], color = 'blue')
    
    #Plotting labels and legend
    
    plt.xlabel("Total Motives", fontsize = "15")
    plt.ylabel("States", fontsize = "15")
    plt.title("Murder Motives", fontsize = "15")
    plt.legend()
    plt.show() 
    
    
    
    #Returning for the Horizontal Bar Graph 
    
    return 
    
    #Defining the Pie function  
    

def motives_of_murder(data,lab_list):
    '''
    

    Parameters
    ----------
    data : TYPE pandas 
        DESCRIPTION.
    lab_list : TYPE 
        DESCRIPTION.

    Returns
    Rsulting shows pie graph
    -------
    None.

    '''
    
    
    
    #Plotting labels and legend
    
    exp=(0 ,0.30, 0, 0, 0)
    plt.pie(data, labels = lab_list, shadow=True, autopct='%6.2f%%', explode = exp)
    plt.title('Terrorists/ Extremists Motives')
    plt.legend(fontsize = 7, loc = 'lower left')   
    
    


 #Reading the csv file 2
tm=pd.read_csv\
     ('Murder Motives.csv')
print(tm)
 
 #Selecting the first seven rows
 
a=tm.head(7)
print(a)
print(a[["STATE"]])
print(Total_motives(a,'STATE','Total'))


#Reading the csv file 2
mm=pd.read_csv\
    ('Murder Motives.csv')
print(mm)
    #Selecting the first five rows
a=mm.head()
print(a)
b=mm['STATE'].head()   
c=mm['Terrorists/ Extremists'].head()

#Calling the function

US_Immigration_Statistics()
motives_of_murder(c,b)



