import numpy as np
from sklearn.cluster import KMeans
from sklearn import datasets
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import plotting_functions

"""
def create_pixel_array():
	with open('IMG_2571.jpg') as f: #when this is closed, image is closed
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
"""
#run KMeans
def kmeans(n_clusters, init, max_iter, sample):
	est = KMeans(n_clusters, init, max_iter)
	est.fit(sample)
	labels = est.predict(sample)
	n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)	

	az = plotting_functions.create_plots('az','KMeans Clusters')

	def kplot(cluster_type, sample):
		kmeans_plot_points = []
		for i in cluster_type:
			for j in i:
				loc = sample[j]
				kmeans_plot_points.append(loc)
		return kmeans_plot_points

	def plot_point_k(atype, color, marker, x,y,z):
		plotting_functions.scatter_plot(atype, x, y, z, color, marker)

	def points_kmeans(cluster_loc,sample):
		kmeans_plot_points = kplot(cluster_loc,sample)
		sample_plot = []
		for point in kmeans_plot_points:
			if random.random() < 300 / float(len(kmeans_plot_points)):
				sample_plot.append(point)
		return sample_plot

	def plot_kmeans(r,g,b,marker):
		color = plotting_functions.convert_to_string_color(r,g,b)
		atype = az
		for point in sample_plot:
			plot_point_k(atype, color, marker, *point)

	cluster_label = 0
	while cluster_label >= 0 and cluster_label < n_clusters_:
		cluster_loc = np.where(labels == cluster_label)
		sample_plot = points_kmeans(cluster_loc, sample)
		r,g,b = sample_plot[0]
		plot_kmeans(r,g,b,"o")
		cluster_label += 1

		"""
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
			plot_point_k(atype, color, marker, *point)
		cluster_label += 1
		"""
	return n_clusters_

