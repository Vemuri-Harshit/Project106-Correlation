import plotly.express as px;
import numpy as np;
import csv;

def getDataSource_data1(data_path):
    marks = []
    attendance = []

    with open(data_path) as data_file: 
        csv_reader = csv.DictReader(data_file);
        for row in csv_reader : 
            marks.append(float(row["marks"]))
            attendance.append(float(row["attendance"]))

    return{"x": attendance, "y": marks}

def findCorrelation_data1(data_source) : 
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation for marks and attendance is", correlation[0,1])

findCorrelation_data1( getDataSource_data1("./data_1.csv") )



def getDataSource_data2(data_path):
    coffee = []
    sleep = []

    with open(data_path) as data_file: 
        csv_reader = csv.DictReader(data_file);
        for row in csv_reader : 
            coffee.append(float(row["coffee"]))
            sleep.append(float(row["sleep"]))

    return{"x": sleep, "y": coffee}

def findCorrelation_data2(data_source) : 
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation for Sleep and Coffee is", correlation[0,1])

findCorrelation_data2( getDataSource_data2("./data_2.csv") )
          