import matplotlib
from matplotlib import pyplot as plt

def _check_xy_variable_(data=None,var=None):
    if callable(var):
        if data is None: 
            raise Exception(f'Data cant be None: {data}')
        return [var(item) for item in data]

    elif type(var) is range:
        return list(var)

    elif type(var) is list:
        return var

    elif type(var) is str:
        raise Exception(f'Variable cant not be string: {var}')
    else :
        return var
                

def line_plot(data=None,_x=lambda x: x[0],_y=lambda y: y[1],**kwargs):
    # determina a natureza das variáveis _x e _y e age de acordo
    _x = _check_xy_variable_(data,_x)
    _y = _check_xy_variable_(data,_y)

    plt.figure()

    ax = plt.plot(_x,_y)

    if (type(ax) is list) and len(ax) == 1:
        ax =  ax[0]

    if kwargs.get('output_file') : 
        save_figure(ax,output_file=kwargs.get('output_file'))

def save_figure(fig,output_file='figure.png',**kwargs):
    
    if type(fig) == matplotlib.lines.Line2D:
        fig.get_figure().savefig(output_file)
    else :
        raise Exception(f'figure type: {type(fig)}')