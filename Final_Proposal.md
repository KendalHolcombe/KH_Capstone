# KH_Capstone

In recent years, advanced technology is changing the way law enforcement agencies across the globe do just about everything. Amidst the increasing number of criminal activities across the world, law enforcement agencies are using big data analytics to combat crime within minimal timelines.

This trend, popularly known as [predictive policing](https://en.wikipedia.org/wiki/Predictive_policing), is gaining popularity in the United States, as well as the UK and China, where the authorities are not just using data to understand past criminal activities, but are also trying to predict future crime. I want to build a model using statistical algorithms that leverages crime data in conjunction with municipal metadata to identify the safest places to live.

There are several instances where law enforcement agencies are using [big data analytics](http://www.govtech.com/data/Role-of-Data-Analytics-in-Predictive-Policing.html) to predict, detect and combat criminal activities. Notably in the US, several police-led initiatives are making the most of surveillance information to identify and prevent crime. Much of the current methods are still reactionary.

For example, some [models](http://www.stat.ucla.edu/~frederic/papers/crime1.pdf) used are [self-exciting point processes](http://mathworld.wolfram.com/Self-ExcitingPointProcess.html), originally developed for modeling earthquake aftershock distributions. The fact that these models fit earthquake and crime event data remarkably well is, on its own, a cool result. Specifically, self-excitation is found in gang violence data as a gang shooting is likely to incite retaliatory violence in the area (territory) of the rival gang. This kind of localized contagious spread of crime leads to the formation of crime clusters. Similarly the occurrence of an earthquake is well known to increase the likelihood of another earthquake nearby. Preventing additional gang violence after a shooting is both preventative and reactionary because the inciting incident must occur first in order to leverage these models to prevent the additional violence.

I would like to uncover a correlation between municipalities locations and crime data to determine the safest place to live based on a person's age and gender. By first grouping the populus into age groups for each gender, I aim to rank specific crimes, murder or arson for example, in decreasing order of likelihood to impact each age group and gender. From there, I will attempt to find a correlation between specific crimes and specific municipalites/locations.  Using this information together I will build a tool to determine the safest place for anyone to live.

**Presentation:**
Using an interactive web app, the user can input a few personal details to return a sorted list of safest places to live, in other words, the safest place for a person of a specific age and gender to live to avoid the crimes which impact them the most. Perhaps to take it a step further, they can specify which crimes they would like to avoid and again have a sorted list of places returned. If they wish to avoid arson, does the number and proximity of fire houses play a role?

**Data:**
I have built a 50+ table database of FBI crime data, census data, and additional metadata
  * [FBI Uniform Crime Reporting](https://www.fbi.gov/services/cjis/ucr)
  * [United States Census Bureau](https://www.census.gov/data/tables.html)
  * [Homeland Infastructure](https://hifld-geoplatform.opendata.arcgis.com/datasets/de0b8dafb352444b9e6cc302499df933_0)

![alt text](https://cdn-images-1.medium.com/max/800/1*lZrXmWJRDLqIImJThs5Lrw.png)

One issue I encountered while gathering and compiling my data was to have a consistant feature for location information. The varying data sources used differing notations for locations, some using latitude and longitude and others using addresses. By converting these to Federal Information Processing Standards(FIPS), unique codes to identify specific geographic areas, I can homogenize the location element across all datasets.

**Next Steps:**

1. Polish my SQL queries for extracting the needed data for my models from my database
2. Exploratory Data Analysis
3. Build a first pass model
4. Evaluate model, determine necessary adjustments, and repeat
