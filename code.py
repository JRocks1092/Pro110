import pandas as pd
import random
import plotly.figure_factory as ff
import statistics
import scipy

df = pd.read_csv("data.csv")
reading_time = df["reading_time"].tolist()
means = []


def sample100_average():
    inte = random.randint(1, len(reading_time)-31)
    test = reading_time[inte:inte+30]
    mean = statistics.mean(test)
    means.append(mean)


for i in range(1, 100):
    sample100_average()

mean_final = statistics.mean(means)
print("final mean is(without sampling) "+str(statistics.mean(reading_time)))
print("final mean is "+str(mean_final))
print("standard deviation "+str(statistics.stdev(reading_time)))

fig = ff.create_distplot([means], ["temp"], show_hist = False)
fig.show()