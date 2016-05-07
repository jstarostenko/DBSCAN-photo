#from PIL import Image
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
import plotting_functions
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def dbscan(eps, min_samples,sample):
    db = DBSCAN(eps=eps, min_samples=min_samples).fit(sample)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

    ay = plotting_functions.create_plots('ay','DBSCAN Clusters')

    def dbplot(cluster_type,sample):
        dbscan_plot_points = []
        for i in cluster_type:
            for j in i:
                loc = sample[j]
                dbscan_plot_points.append(loc)
        return dbscan_plot_points

    def plot_point_db(atype, color, marker, x,y,z):
        plotting_functions.scatter_plot(atype, x, y, z, color, marker)

    def points_dbscan(cluster_loc,sample):
        dbscan_plot_points = dbplot(cluster_loc,sample)
        sample_plot = []
        for point in dbscan_plot_points:
            if random.random() < 300 / float(len(dbscan_plot_points)):
                sample_plot.append(point)
        return sample_plot

    def plot_dbscan(r,g,b,marker):
        color = plotting_functions.convert_to_string_color(r,g,b)
        atype = ay
        for point in sample_plot:
            plot_point_db(atype, color, marker, *point)

    cluster_label = 0
    while cluster_label >= 0 and cluster_label < n_clusters_:
        cluster_loc = np.where(labels == cluster_label)
        sample_plot = points_dbscan(cluster_loc, sample)
        r,g,b = sample_plot[0]
        plot_dbscan(r,g,b,"o")
        cluster_label += 1

    else:
        cluster_loc = np.where(labels == -1)
        sample_plot = points_dbscan(cluster_loc,sample)
        r,g,b = (22,22,22)
        plot_dbscan(r,g,b,"+")

    return n_clusters_
