import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_plots(atype1,atype2,no_clusters):
	fig = plt.figure(figsize=(7,7), dpi=120)
	fig2 = plt.figure(figsize=(7,7), dpi=120)
	atype1 = fig.add_subplot(111, projection='3d')
	atype2 = fig2.add_subplot(111, projection='3d')
	
	atype1.set_xlabel('Red Component')
	atype1.set_ylabel('Green Component')
	atype1.set_zlabel('Blue Component')
	atype1.set_xbound(0,255)
	atype1.set_ybound(0,255)
	atype1.set_zbound(0,255)
	fig.suptitle('Estimated Number of Clusters: %d' % no_clusters)

	atype2.set_xlabel('Red Component')
	atype2.set_ylabel('Green Component')
	atype2.set_zlabel('Blue Component')
	atype2.set_xbound(0,255)
	atype2.set_ybound(0,255)
	atype2.set_zbound(0,255)
	fig2.suptitle('Sample Pixels')

	return atype1, atype2

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