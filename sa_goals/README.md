This repository is a collection of files for the creation of a choropleth map page

Data was collected from the appropriate people in an Excel file. A python script runs
to turn the individual cell values into the appropriate inputs for the choropleth map
and saved as a csv.

Using D3, the csv file is processed into a geojson using a blank us-states.json file,
merging on the full state name. This json is then used to color the choropleth and 
populate the panel below the map.

Copyright: Aaron Holm, 2019
