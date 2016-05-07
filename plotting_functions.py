import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

def create_plots(atype,title):
    fig = plt.figure(figsize=(7,7), dpi=120)
    atype = fig.add_subplot(111, projection='3d')

    atype.set_xlabel('Red Component')
    atype.set_ylabel('Green Component')
    atype.set_zlabel('Blue Component')
    atype.set_xbound(0,255)
    atype.set_ybound(0,255)
    atype.set_zbound(0,255)
    fig.suptitle(title)

    return atype

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

def plot_sample_pixels(pixel_array,pixel_quant,atype):
    for point in pixel_array:
        if random.random() < pixel_quant / float(len(pixel_array)):
            plot_point(atype, *point)
