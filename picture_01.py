from bokeh.charts import Histogram, output_file, show
from bokeh.charts import defaults, vplot, hplot, show, output_file
from bokeh.plotting import figure, show, output_file
from bokeh.io import push_notebook
#from bokeh.sampledata.autompg import autompg as df
import pandas as pd
import numpy as np
import PIL
from PIL import Image

lena_img = Image.open('Euro2016_Final_Twitter_Word_Cloud_02.png').convert('RGBA')
xdim, ydim = lena_img.size
print("Dimensions: ({xdim}, {ydim})".format(**locals()))
# Create an array representation for the image `img`, and an 8-bit "4
# layer/RGBA" version of it `view`.
img = np.empty((ydim, xdim), dtype=np.uint32)
view = img.view(dtype=np.uint8).reshape((ydim, xdim, 4))
# Copy the RGBA image into view, flipping it so it comes right-side up
# with a lower-left origin
view[:,:,:] = np.flipud(np.asarray(lena_img))

# Display the 32-bit RGBA image
dim = max(xdim, ydim)
fig = figure(title="Word_Cloud",
             x_range=(0,dim), y_range=(0,dim),
             # Specifying xdim/ydim isn't quire right :-(
             # width=xdim, height=ydim,
             )
fig.image_rgba(image=[img], x=0, y=0, dw=xdim, dh=ydim)

output_file("word_cloud.html", title="image example")

show(fig) 
