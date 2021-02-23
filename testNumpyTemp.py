import numpy as np
fp = "Dataset.txt"
data = np.genfromtxt(fp, skip_header=1, usecols=(0, 1, 2, 3))
print (data)
date=data[:,0]
print (date)
t_AVG = data[:,1]
t_MIN = data[:,2]
t_MAX = data[:,3]
print (t_AVG)
print (t_MIN)
print (t_MAX)
date_mask = np.isfinite(date)

print("Number of years:", np.count_nonzero(date_mask))

missing_date_mask = ~np.isfinite(date)

print("Number of missing years:", np.count_nonzero(missing_date_mask))

t_AVG_mask = np.isfinite(t_AVG)
print("Number of avg temps:", np.count_nonzero(t_AVG_mask))

missing_t_MAX_mask = ~np.isfinite(t_MAX)
print("NUmber of misisng T_MAX values:", np.count_nonzero(missing_t_MAX_mask))
tmax_mask = np.isfinite(t_MAX)

tmax_clean = t_MAX[tmax_mask]
print (tmax_clean)
date_clean = date[tmax_mask]

tmax_total = tmax_clean[(date_clean >= 1973 & (date_clean < 2010))]
print (tmax_total)
print(tmax_total.mean())