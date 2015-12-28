import numpy as np
import matplotlib.pyplot as plt
import random
import import_pixels
import plotting_functions
import photo_dbscan
import photo_kmeans

a = import_pixels.imp_pixels('IMG_2549.jpg')

#generate sample data:
sample = []
for point in a:
	if random.random() < 500 / float(len(a)):
		sample.append(point)
sample = np.asarray(sample)

#plot sample pixels
ay = plotting_functions.create_plots('ay','Sample Pixels')
plotting_functions.plot_sample_pixels(a,1000,ay)

#run DBSCAN and plot sample points:
##is this format ok?
eps = 10
min_samples = 5
n_clusters_dbscan = photo_dbscan.dbscan(eps,min_samples,sample)
print('Estimated Number of DBSCAN Clusters: %d' % n_clusters_dbscan)

#run KMeans and plot sample points:
n_clusters = 5
init = 'random'
max_iter = 3000
n_clusters_kmeans = photo_kmeans.kmeans(n_clusters, init, max_iter, sample)
print ('Number of KMeans Clusters: %d' % n_clusters_kmeans)

plt.show()
