# Finnish_Population

My very first test project to see what kind of GIS-visualizations can be done with a simple Python script. In this project I made a 3d animation of the population changes in Finnish Municipalities since 1990-2019. The script also includes the code to save the animation as a mp4-video.  

Data sources:

-Finnish Municipality population from Statistics Finland's open data: 
http://pxnet2.stat.fi/PXWeb/pxweb/en/StatFin/StatFin__vrm__vaerak/statfin_vaerak_pxt_11ra.px/

-Coordinate points of Finnish Municipalities: 
https://fi.wikipedia.org/wiki/Luettelo_Suomen_kuntien_koordinaateista

-Finnish borderline as shp-file:
https://tiedostopalvelu.maanmittauslaitos.fi/tp/kartta?lang=en


Yet not finished/figured out:

-Script doesn't yet include the Matplotlib Basemap Toolkit so no map projection is determined. Thus the map looks squished.

-Haven't yet figured how to color the bars according to a colormap.

-Would be pretty cool if the script could just get the population data online. StatFin Statistics Finland's online service provides a possibility to do this but haven't yet figured how it works.
