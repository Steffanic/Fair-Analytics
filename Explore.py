import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

FILELIST = ["Data/Class 1/20%s.csv"%(str(x).zfill(2)) for x in range(1, 19)]

def log(msg="Hello World"):
    print("Log: ", msg)

def read_in_data(filename="Data/Class 1/2001.csv"):
    log(f"Reading in {filename}")
    dat=pd.read_csv(filename, encoding='cp1252')
    dat.set_index("Fair Name", inplace=True)
    return dat

def type_data(dat):
    for col in dat.columns:
        dat[col] = pd.to_numeric(dat[col], errors='coerce')

def plot_columns(dat):
    fig=plt.figure(figsize=(10,10))
    for col in dat.columns:
        dat[col].plot()
        plt.ylabel(col)
        plt.xticks(range(len(dat)), labels=dat.index ,rotation=90)
        plt.tight_layout()
        plt.show()

def write_columns_out(dat):
    with open("Yearly_Columns.txt", 'a') as f:
        for col in dat.columns:
            f.write(col)
            f.write(", ")
        f.write("\n")

if __name__=="__main__":
    for fname in FILELIST:
        log(fname)
        if not os.path.exists(fname):
            continue
        dat = read_in_data(fname)
        type_data(dat)
        write_columns_out(dat)
        #plot_columns(dat)