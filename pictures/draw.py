import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import datetime as dt
import matplotlib.dates as mdates
import json
from pprint import pprint


style.use('ggplot')


def draw(title):

    date = []
    y = []

    filename = title + '.json'
    with open(filename, 'r') as f:
        data = json.load(f)
    for item in data['values']:
        date.append(item['x'])
        y.append(item['y'])
    ylabel = data['unit']
    title = data['name']
    title = title + '\n\n' + data['description']
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    dateconv = np.vectorize(dt.datetime.fromtimestamp)
    date = dateconv(date)

    ax1.plot_date(date, y, '-')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True)  # , color='g', linestyle='-', linewidth=5)

    plt.xlabel('Date')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    # plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94,
    #                     top=0.90, wspace=0.2, hspace=0)
    plt.show()

draw('transactions-per-block')
