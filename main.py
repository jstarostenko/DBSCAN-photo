import numpy as np
import matplotlib.pyplot as plt
import random
import import_pixels
import plotting_functions
import photo_dbscan
import photo_kmeans

def main():
    a = import_pixels.import_pixels('IMG_2549.jpg')

    #generate sample data:
    sample = []
    for point in a:
        if random.random() < 500 / float(len(a)):
            sample.append(point)
    sample = np.asarray(sample)

    #plot sample pixels
    ax = plotting_functions.create_plots('ax','Sample Pixels')
    plotting_functions.plot_sample_pixels(a,1000,ax)

    #run DBSCAN and plot sample points:
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

if __name__=="__main__":
    main()
