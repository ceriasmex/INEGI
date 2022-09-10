# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def process():
    import pandas as pd
    import numpy as np

    file="INE_ENTIDAD_2020.CSV"
    dfstate=pd.read_csv(file, encoding = "ISO-8859-1")
    dfstate['ENT'] = list(range(len(dfstate.index)))

    print(dfstate.columns.tolist())
    totalpop=dfstate['POBTOT'].sum()
    maxstate=dfstate.idxmax()
    minstate=dfstate.idxmin()
    print("Total population: " + str(totalpop))
    print(str(maxstate))
    totpob=0

    print(type(minstate))

    for i in range(len(dfstate)):
    #for i in range(1):
        state=dfstate.loc[i,["NOM_ENT ", "POBTOT"]]
        totpob =totpob + state[1]

    maxstate=dfstate["POBTOT"].idxmax()
    totpob= '{:,}'.format(totpob)
    maxnstate=dfstate.loc[maxstate,["POBTOT"]]
    nstate=dfstate.loc[maxstate,["NOM_ENT "]]
    print("Total pob:" + str(totpob)+" " +str(maxnstate[0]) + " " + str(nstate[0]))

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to rPun the script.
if __name__ == '__main__':
    process()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/