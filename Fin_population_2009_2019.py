import mpl_toolkits.mplot3d.axes3d as p3                                                                #Library for basic 3D plotting tools
import matplotlib.pyplot as plt                                                                         #Matplotlib-library for plotting data
import numpy as np                                                                                      #Library for math functions
import pandas as pd                                                                                     #Library for data analysis
import shapefile as shp                                                                                 #Pyshp library for visualizing shp geospatial vector data
import matplotlib.animation as animation                                                                #Library for animating data
#plt.rcParams['animation.ffmpeg_path'] = 'your_path/ffmpeg/bin/ffmpeg.exe'                             #Path to ffmpeg. Need this if you want to save animation as video. https://ffmpeg.org/

fig = plt.figure()                                                                                      #"The top level container for all the plot elements".
ax = p3.Axes3D(fig)                                                                                     #Determine axis to be 3d-axis
#Writer = animation.writers['ffmpeg']                                                                   #Set up formatting for the movie files
#writer = Writer(fps=5, metadata=dict(artist='Me'), bitrate=1800)                                       #Set up formatting for the movie files

sf = shp.Reader('your_path/Finland_wgs84.shp')                                                          #Loading the Finnish borderlines. Original coordinate system ETRS-TM35FIN, coordinate transformation done in QGIS.


df = pd.read_csv('your_path/Finnish_population.csv',                                                    #Determine dataframe. CSV-file built with Pandas merge function. Original coordinates picked from site: https://fi.wikipedia.org/wiki/Luettelo_Suomen_kuntien_koordinaateista
                 delimiter=',', encoding="utf-8")
#print(df.head(10))                                                                                     #Print first 10 rows of dataframe                                                                             

df['x_width'] = float(0.3)                                                                              #Create a new column "x_width". Data will contain values for bar width. Alla bars will be same size
df['y_width'] = float(0.3)                                                                              #Create a new column "y_width". Data will contain values for bar width. Alla bars will be same size
year_columns = [df['1990'], df['1991'], df['1992'], df['1993'], df['1994'], df['1995'], df['1996'],     #List of columns containing yearly data of population.
                df['1997'], df['1998'], df['1999'], df['2000'], df['2001'], df['2002'], df['2003'],
                df['2004'], df['2005'], df['2006'], df['2007'], df['2008'], df['2009'], df['2010'],
                df['2011'], df['2012'], df['2013'], df['2014'], df['2015'], df['2016'], df['2017'],
                df['2018'], df['2019']]

graph_heading = [1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,  #Ugly looking workaround for graph headings. Would be better to get headings from dataframe columns in in year_column. Haven't figured how.
              2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]

graph = []                                                                                              #Will be our list of 3D bars. Empty list at the beginning. When generating multiple bars, x, y, z have to be arrays. dx, dy, dz can be arrays or scalars.
xpos = df['X']                                                                                          #Xcoordinate on map
ypos = df['Y']                                                                                          #Ycoordinate on map
zpos = np.zeros(len(df['X']))                                                                           #Zcoordinate. All zeros so the bars start from bottom. Return an array of zeros, length of column X.
dx = df['x_width']                                                                                      #Width(x) of bars. Determined earlier.
dy = df['y_width']                                                                                      #Width(y) of bars. Determined earlier.
dz =[]                                                                                                  #Height(z) of bars. At the beginning an empty list.

def bars(i):                                                                                            #Function for updating the bar heights
        dz = year_columns[i]                                                                            #Iterates through the list year_columns. Bar heights are updated through each cycle.
        ax.clear()                                                                                      #After updating the new height, we clear the last results. Makes animation much faster.
        ax.set_axis_off()
        ax.set_zlim3d([0.0, 500000.0])                                                                  #For visual purpose, we limit the z-axis making it stay static.                                                                          
        graph = ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color = 'r')                                     #The 3D bar values are collect into the list determined earlier. https://matplotlib.org/mpl_toolkits/mplot3d/api.html.
        ax.set_title(graph_heading[i])                                                                  #After each iteration, sets graph title as value in list graph_head
        for shape in sf.shapeRecords():                                                                 #Showing the Finnish borders
            x = [i[0] for i in shape.shape.points[:]]
            y = [i[1] for i in shape.shape.points[:]]
        plt.plot(x,y)
        return graph                                                                                    #Returns the list of 3d bars with updated values. Return is used to end the execution of the function call and “returns” the result to the caller. The statements after the return statements are not executed.

ani = animation.FuncAnimation(fig, bars, frames=len(year_columns),interval=20, cache_frame_data=False)  #Creating the animation. https://matplotlib.org/3.3.0/api/_as_gen/matplotlib.animation.FuncAnimation.html. Disabling cache seems helpful when frame contain large number of objects.
#ani.save('im1.mp4', writer=writer)                                                                     #Saving the animation as mp4

plt.show()                                                                                              #Show animation
