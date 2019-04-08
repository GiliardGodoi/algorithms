import matplotlib
from matplotlib import pyplot as plt


def line_plot(data,_x=lambda x: x[0],_y=lambda y: y[1],**kwargs):     

    _x = [ i for i in range(1,len(data)+1)]
    _y = [ r[1] for r in data ]
    # _z = [ r[1] for r in self.__statisticsData ]

    ax = plt.plot(_x,_y)[0]

    if kwargs.get('output_file') : save_figure(ax,*kwargs)

def save_figure(fig,output_file='figure.png'):
    
    if type(fig) == matplotlib.lines.Line2D:
        fig.get_figure().savefig(output_file)