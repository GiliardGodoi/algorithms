import statistics 
from statistics import mean
from statistics import pvariance
from matplotlib import pyplot as plt
import csv


class Logger():

    def __init__(self,**kwargs):
        self.__statisticsData = list()

    def get_statistics_data(self):
            return self.__statisticsData

    def logger(self,data,**kwargs):
        record = [mean(data),pvariance(data)]
        if kwargs.get('iteration') :
            record = [kwargs.get('iteration')] + record

        self.__statisticsData.append(record)

    def draw_chart(self):
        
        ax = plt.axes()
        
        _x = [ i for i in range(1,len(self.__statisticsData)+1)]
        _y = [ r[1] for r in self.__statisticsData ]
        # _z = [ r[1] for r in self.__statisticsData ]

        ax.plot(_x,_y)[0]

        ax.get_figure().savefig('teste.png')

    