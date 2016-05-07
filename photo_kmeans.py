import numpy as np
from sklearn.cluster import KMeans
from sklearn import datasets
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import plotting_functions

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

    return n_clusters_

