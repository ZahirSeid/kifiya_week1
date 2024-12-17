import matplotlib.pyplot as plt

def plot_bar(data, title, xlabel, ylabel):
    """
    Plots a bar chart.
    """
    data.plot(kind="bar", title=title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plot_line(data, title, xlabel, ylabel):
    """
    Plots a line chart.
    """
    data.plot(kind="line", title=title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

