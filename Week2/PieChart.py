# Name: Chris Chausse
# Date: 4-7-25
# Assignment CS 162 Graphic File Exercise (Week 2)


# Import matplotlib library
import matplotlib.pyplot as plot

# Where names and values for the number of each class, and order displayed on the chart as well
numlist = [7, 10, 6, 4]
namelist = ['Junior', 'Sophomores', 'Freshman', 'Seniors']

# Where colors are set, and the offset of the "largest" class can be offset to pull in the reader
colorlist = ['orange', 'red', 'cyan', 'yellow' ]
explodelist = [0.0, 0.1, 0.0, 0.0]

# Where the piechart is created with whatever visual/formatting parameters one wishes to add 
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist, explode = explodelist, startangle = 292,
         shadow = True, wedgeprops={'edgecolor': 'black', 'linewidth': 0.5},
         textprops={'fontsize': 12, 'fontweight': 'bold'}, radius=1.25)

# Ensures X and Y axis are equal scale/size so it is perfectly round
plot.axis('equal')

# This is where the file is saved to the chosen directory/location
plot.savefig('./piechart.png')