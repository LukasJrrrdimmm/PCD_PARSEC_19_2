import numpy as np
import math as mth
import matplotlib.pyplot as plt
import pandas as pd


cores = np.array(list(map(float, input().split())))
program_ndf = {}
speedup_ndf = {}
efficiency_ndf = {}
mean_ndf = {}
med_program_ndf = {}
med_speedup_ndf = {}
med_efficiency_ndf = {}
median_ndf = {}
df_index = []
df_indexb = []

while 1:
  try:
    sr = str(input())
    df_indexb.append(str("n = {}".format(sr)))
    data = {}
    df_index = []
    for i in range(0, len(cores)):
      aux = np.array(list(map(float, input().split())))
      if cores[i] == 1:
        data['Serial'] = aux
        df_index.append('Serial')
      else:
        auxb = str("Parallel {} cores".format(cores[i]))
        df_index.append(auxb)
        data[auxb] = aux
    df_data = pd.DataFrame(data)
    df_mean = df_data.mean()
    df_median = df_data.median()
    print(df_data)
    print(df_mean)
    program_ndf[sr] = df_data
    mean_ndf[sr] = df_mean
    median_ndf[sr] = df_median
    speedup_ndf[sr] = df_mean/df_mean['Serial']
    med_speedup_ndf[sr] = df_median/df_median['Serial']
    efficiency_ndf[sr] = speedup_ndf[sr]/np.array(cores)
    med_efficiency_ndf[sr] = med_speedup_ndf[sr]/np.array(cores)
    
  except EOFError:
    break;
pd_mean_ndf = pd.DataFrame(mean_ndf)
pd_speedup_ndf = pd.DataFrame(speedup_ndf)
pd_efficiency_ndf = pd.DataFrame(efficiency_ndf)
pd_mean_ndf.columns = df_indexb
pd_speedup_ndf.columns = df_indexb
pd_efficiency_ndf.columns = df_indexb
pd_median_ndf = pd.DataFrame(median_ndf)
pd_med_speedup_ndf = pd.DataFrame(med_speedup_ndf)
pd_med_efficiency_ndf = pd.DataFrame(med_efficiency_ndf)
pd_median_ndf.columns = df_indexb
pd_med_speedup_ndf.columns = df_indexb
pd_med_efficiency_ndf.columns = df_indexb
#pd_mean_ndf.index = df_index
print("mean time: real")
print(pd_mean_ndf)
print("mean Speedup")
print(pd_speedup_ndf)
print("mean Efficiency")
print(pd_efficiency_ndf)
pd_mean_ndf.plot(kind = 'bar').grid()
plt.title("time: real (mean)")
plt.show()
pd_speedup_ndf.plot(kind = 'bar').grid()
plt.title("Speedup (mean)")
plt.show()
pd_efficiency_ndf.plot(kind = 'bar').grid()
plt.title("Efficiency (mean)")
plt.show()
print("median time: real")
print(pd_median_ndf)
print("median Speedup")
print(pd_med_speedup_ndf)
print("median Efficiency")
print(pd_med_efficiency_ndf)
pd_median_ndf.plot(kind = 'bar').grid()
plt.title("time: real (median)")
plt.show()
pd_med_speedup_ndf.plot(kind = 'bar').grid()
plt.title("Speedup (median)")
plt.show()
pd_med_efficiency_ndf.plot(kind = 'bar').grid()
plt.title("Efficiency (median)")
plt.show()
print("\nScallability Degree")
print(pd_efficiency_ndf[df_indexb[2] ])
g = pd_efficiency_ndf[df_indexb[2]] - pd_efficiency_ndf[df_indexb[1]]
print(pd_efficiency_ndf[df_indexb[2]] - pd_efficiency_ndf[df_indexb[1]])
print(g/(0 + pd_efficiency_ndf[df_indexb[1]]))
scalability_degree_mean = {}
scalability_degree_median = {}
for i in range(0, len(df_indexb) - 1):
  print(df_indexb[i])
  n = i +1
  a = str("Scal ({}".format(n) + " -> {})".format([i]))
  scalability_degree_mean[a] = (pd_efficiency_ndf[df_indexb[n]] - pd_efficiency_ndf[df_indexb[i]])/(0 + pd_efficiency_ndf[df_indexb[i]])
  scalability_degree_median[a] = (pd_med_efficiency_ndf[df_indexb[n]] - pd_med_efficiency_ndf[df_indexb[i]])/(0 + pd_med_efficiency_ndf[df_indexb[i]])
pd_scal_deg_mean = pd.DataFrame(scalability_degree_mean)
print("Scalability Darta Frame")
print(pd_scal_deg_mean)
pd_scal_deg_median = pd.DataFrame(scalability_degree_median)
pd_scal_deg_mean.plot(kind = 'bar').grid()
plt.title("Scalability Coeficient (mean)")
plt.show()
print(pd_scal_deg_median)
pd_scal_deg_median.plot(kind = 'bar').grid()
plt.title("Scalability Coeficient (median)")
plt.show()

