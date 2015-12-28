from PIL import Image
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import import_pixels
import plotting_functions

a = import_pixels.imp_pixels('IMG_2549.jpg')


"""
#open image file and extract pixel data
def create_pixel_array():
	with open('IMG_2571.jpg') as f: #when this is closed, image is closed
		image = Image.open(f)
		return np.array(image, dtype = np.int16)

pixel_array = create_pixel_array()

a = []
for i in pixel_array:
	for j in i:
		a.append(j)
"""
#plot sample points:

#generate sample data:
sample = []
for point in a:
	if random.random() < 500 / float(len(a)):
		sample.append(point)
sample = np.asarray(sample)
print sample.shape


#run DBSCAN:
db = DBSCAN(eps=10, min_samples=5).fit(sample)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_
print "labels array:", labels
print labels.shape
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print('Estimated number of clusters: %d' % n_clusters_)	

ax,ay = plotting_functions.create_plots('ax','ay', n_clusters_)

sample = []
for point in a:
	if random.random() < 1000 / float(len(a)):
		plotting_functions.plot_point(ay, *point)

"""
fig = plt.figure(figsize=(7,7), dpi=120)
fig2 = plt.figure(figsize=(7,7), dpi=120)
ax = fig.add_subplot(111, projection='3d')
ay = fig2.add_subplot(111, projection='3d')
"""
"""
def convert_to_string_color(r,g,b):
    r_str = ("0x%0.2X" % r)[-2:]
    g_str = ("0x%0.2X" % g)[-2:]
    b_str = ("0x%0.2X" % b)[-2:]
    return "#" + r_str + g_str + b_str

def scatter_plot(atype,x,y,z,color,marker):
	atype.scatter(x,y,z, c=color, marker = marker, depthshade=False)

def plot_point(atype,x,y,z):
	color = convert_to_string_color(x,y,z)
	scatter_plot(atype, x, y, z, color, "o")
"""



#determine locations of DBSCAN points:
def dbplot(cluster_type):
	dbscan_plot_points = []
	for i in cluster_type:
		for j in i:
			loc = sample[j]
			dbscan_plot_points.append(loc)
	#provide list of points that are associated with label x
	print "dbscan_plot_points shape:", dbscan_plot_points.shape
	return dbscan_plot_points

def plot_point_db(atype, color, marker, x,y,z):
	plotting_functions.scatter_plot(atype, x, y, z, color, marker)

def points_dbscan():
	dbscan_plot_points = dbplot(cluster_loc)

	sample_plot = []
	for point in dbscan_plot_points:
		if random.random() < 300 / float(len(dbscan_plot_points)):
			sample_plot.append(point)
	return sample_plot

def plot_dbscan(r,g,b,marker):
	color = plotting_functions.convert_to_string_color(r,g,b)
	atype = ax
	for point in sample_plot:
		plot_point_db(atype, color, marker, *point)

cluster_label = 0
while cluster_label >= 0 and cluster_label < n_clusters_:
	#determine location in labels array where label is set to x
	cluster_loc = np.where(labels == cluster_label)
	#gather 
	sample_plot = points_dbscan()
	r,g,b = sample_plot[0]
	#plot these points
	plot_dbscan(r,g,b,"o")
	#move to next label x
	cluster_label += 1

else:
	cluster_loc = np.where(labels == -1)
	sample_plot = points_dbscan()
	r,g,b = (22,22,22)
	plot_dbscan(r,g,b,"+")


plotting_functions.format_plots(ax,ay,fig,fig2)

"""
#format plots
ax.set_xlabel('Red Component')
ax.set_ylabel('Green Component')
ax.set_zlabel('Blue Component')
ax.set_xbound(0,255)
ax.set_ybound(0,255)
ax.set_zbound(0,255)
fig.suptitle('Estimated Number of Clusters: %d' % n_clusters_)

ay.set_xlabel('Red Component')
ay.set_ylabel('Green Component')
ay.set_zlabel('Blue Component')
ay.set_xbound(0,255)
ay.set_ybound(0,255)
ay.set_zbound(0,255)
fig2.suptitle('Sample Pixels')
"""

plt.show()