import pandas as pd

def inn(var1,var2):
    cond1 = df.loc[:, "Segment"] == var1
    cond2 = df.loc[:, "Country"] == var2
    a = df.loc[cond1 & cond2]
    x = a.loc[:,"Product"].sample(n=1).values[0]
    out(x)

def out(x):
    with open('testing.txt', 'r') as file:
        line = file.readlines()
        line[2] = '%%/*28941843*/' + x + ':;%%'
        for i in line:
            print(i)

df = pd.read_excel('testing.xlsx')

var1 = input("Enter the MO : ")
var2 = input("Enter the Parameter ID : ")

inn(var1,var2)