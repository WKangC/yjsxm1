#K-means++
from pylab import *
from numpy import *
import codecs
import matplotlib.pyplot as plt
data=[]
labels=[]

#read
with codecs.open("data.txt","r") as f:
    for line in f.readlines():
        x,y,label=line.strip().split('\t')
        data.append([float(x),float(y)])
        labels.append(float(label))
datas=array(data)
 
#Calculate Euclidean distance
def distance(x1,x2):
    return sqrt(sum(power(x1-x2,2)))
 
#Find the cluster center closest to the sample for a sample
def nearest(point, cluster_centers):
    min_dist = inf
    m = np.shape(cluster_centers)[0]  # The number of cluster centers currently initialized
    for i in range(m):
        # Calculate the distance between the point and each cluster center
        d = distance(point, cluster_centers[i, ])
        # Choose the shortest distance
        if min_dist > d:
            min_dist = d
    return min_dist

#Select the class center as far away as possible
def get_centroids(dataset, k):
    m, n = np.shape(dataset)
    cluster_centers = np.zeros((k , n))
    index = np.random.randint(0, m)
    cluster_centers[0,] = dataset[index, ]
    d = [0.0 for _ in range(m)]
    for i in range(1, k):
        sum_all = 0
        for j in range(m):
            d[j] = nearest(dataset[j, ], cluster_centers[0:i, ])
            sum_all += d[j]
        sum_all *= random.rand()
        for j, di in enumerate(d):
            sum_all=sum_all - di
            if sum_all > 0:
                continue
            cluster_centers[i,] = dataset[j, ]
            break
    return cluster_centers
 
#Main program
def Kmeans(dataset,k):
    row_m=shape(dataset)[0]
    cluster_assign=zeros((row_m,2))
    center=get_centroids(dataset,k)
    change=True
    while change:
        change=False
        for i in range(row_m):
            mindist=inf
            min_index=-1
            for j in range(k):
                distance1=distance(center[j,:],dataset[i,:])
                if distance1<mindist:
                    mindist=distance1
                    min_index=j
            if cluster_assign[i,0] != min_index:
                change=True
            cluster_assign[i,:]=min_index,mindist**2
        for cen in range(k):
            cluster_data=dataset[nonzero(cluster_assign[:,0]==cen)]
            center[cen,:]=mean(cluster_data,0)
    return center ,cluster_assign
cluster_center,cluster_assign=Kmeans(datas,3)
print(cluster_center)
 
#Make a scatter plot
xlim(0, 10)
ylim(0, 10)

f1 = plt.figure(1)
plt.scatter(datas[nonzero(cluster_assign[:,0]==0),0],datas[nonzero(cluster_assign[:,0]==0),1],marker='o',color='r',label='0',s=30)
plt.scatter(datas[nonzero(cluster_assign[:,0]==1),0],datas[nonzero(cluster_assign[:,0]==1),1],marker='+',color='b',label='1',s=30)
plt.scatter(datas[nonzero(cluster_assign[:,0]==2),0],datas[nonzero(cluster_assign[:,0]==2),1],marker='*',color='g',label='2',s=30)
plt.scatter(cluster_center[:,1],cluster_center[:,0],marker = 'x', color = 'm', s = 50)
plt.show() 