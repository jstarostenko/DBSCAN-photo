from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
from sklearn import datasets
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

#open image file and extract pixel data
def create_pixel_array():
	with open('tim.jpg') as f: #when this is closed, image is closed
		image = Image.open(f)
		return np.array(image, dtype = np.float64)

pixel_array = create_pixel_array()

a = []
for i in pixel_array:
	for j in i:
		a.append(j)

fig = plt.figure(figsize=(7,7), dpi=120)
fig2 = plt.figure(figsize=(7,7), dpi=120)
ax = fig.add_subplot(111, projection='3d')
ay = fig2.add_subplot(111, projection='3d')

def convert_to_string_color(r,g,b):
    r_str = ("0x%0.2X" % r)[-2:]
    g_str = ("0x%0.2X" % g)[-2:]
    b_str = ("0x%0.2X" % b)[-2:]
    return "#" + r_str + g_str + b_str

def plot_point_k(color,marker,x,y,z):
	ax.scatter(x, y, z, c=color, marker=marker, depthshade=False)

def plot_point(x,y,z):
	color = convert_to_string_color(x,y,z)
	ay.scatter(x, y, z, c=color, marker="o", depthshade=False)

#generate sample data
sample = []
for point in a:
	if random.random() < 1000 / float(len(a)):
		plot_point(*point)
	if random.random() < 5000 / float(len(a)):
		sample.append(point)
sample = np.asarray(sample)

#run KMeans
est = KMeans(n_clusters=3, init='kmeans++', max_iter=300)
est.fit(sample)
labels = est.predict(sample)
print "Labels:", labels
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print('Number of clusters: %d' % n_clusters_)	

#determine locations of KMeans points:
def kplot(cluster_type):
	kmeans_plot_points = []
	for i in cluster_type:
		for j in i:
			loc = sample[j]
			kmeans_plot_points.append(loc)
	return kmeans_plot_points

cluster_label = 0

while cluster_label >= 0 and cluster_label < n_clusters_:
	cluster_loc = np.where(labels == cluster_label)
	kmeans_plot_points = kplot(cluster_loc)
	#generate sample of sample data to be plotted for DBSCAN
	sample_plot = []
	for point in kmeans_plot_points:
		if random.random() < 300 / float(len(kmeans_plot_points)):
			sample_plot.append(point)
	r,g,b = sample_plot[0]
	marker = "o"
	color = convert_to_string_color(r,g,b)
	for point in sample_plot:
		plot_point_k(color, marker, *point)
	cluster_label += 1

#format plots
ax.set_xlabel('Red Component')
ax.set_ylabel('Green Component')
ax.set_zlabel('Blue Component')
ax.set_xbound(0,255)
ax.set_ybound(0,255)
ax.set_zbound(0,255)
fig.suptitle('Number of Clusters: %d' % n_clusters_)

ay.set_xlabel('Red Component')
ay.set_ylabel('Green Component')
ay.set_zlabel('Blue Component')
ay.set_xbound(0,255)
ay.set_ybound(0,255)
ay.set_zbound(0,255)
fig2.suptitle('Sample Pixels')

plt.show()

