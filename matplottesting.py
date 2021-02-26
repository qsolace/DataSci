import matplotlib
import matplotlib.pyplot as plt
import numpy as np


fp = "Dataset.txt"
data = np.genfromtxt(fp, skip_header=1, usecols=(0, 1, 2, 3))

date=data[:,0]

t_AVG = data[:,1]
t_MIN = data[:,2]
t_MAX = data[:,3]

date_mask = np.isfinite(date)
missing_date_mask = ~np.isfinite(date)
t_AVG_mask = np.isfinite(t_AVG)
missing_t_MAX_mask = ~np.isfinite(t_MAX)
tmax_mask = np.isfinite(t_MAX)
tmax_clean = t_MAX[tmax_mask]
date_clean = date[tmax_mask]

missing_t_MIN_mask = ~np.isfinite(t_MIN)
tmin_mask = np.isfinite(t_MIN)
tmin_clean = t_MIN[tmin_mask]

tmin=tmin_clean[1::5]
tmax=tmax_clean[1::5]
dateFinal = date_clean[1::5]

labels = dateFinal
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]





x = np.arange(len(dateFinal))
width = .4

fig, ax = plt.subplots()
rects1 = ax.bar (x- width/2, tmax, width, label="Maximum")
rects2 = ax.bar (x+ width/2, tmin, width, label="Minimum")

ax.set_ylabel('Temperature (Celcius)')
ax.set_xlabel("Year")
ax.set_title("Annual maximum and minimum temperatures")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel (rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
plt.plot(date_clean, tmin_clean)
fig.tight_layout()

plt.show()
