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

    def log(self,data,**kwargs):
        record = [mean(data),pvariance(data)]

        if kwargs.get('iteration') :
            record = [kwargs.get('iteration')] + record

        self.__statisticsData.append(record)
