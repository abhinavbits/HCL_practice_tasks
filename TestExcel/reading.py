import pandas as pd

def inn(var1,var2):
    cond1 = df.loc[:, "MO"] == var1
    cond2 = df.loc[:, "Parameter ID"] == var2
    a = df.loc[cond1 & cond2]
    x = a.loc[:,"MML Command"].values[0]
    out(x)

def out(x):
    with open('testing.txt', 'r') as file:
        line = file.readlines()
        line[2] = '%%/*28941843*/' + x.strip() + ':;%%'
        for i in line:
            print(i)

df = pd.read_excel('telecom.xlsx')

var1 = input("Enter the MO : ")
var2 = input("Enter the Parameter ID : ")

inn(var1,var2)
