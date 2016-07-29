Getting Started with SimpleGIS
==============================

Installation
------------
You can use pip to install SimpleGIS with one single command in your terminal.
``$ pip install SimpleGIS``

Find out current location information
-------------------------------------
SimpleGIS provides simple-to-use APIs for access locations infomation. Let's explore how we can get the current location information.

We start by importing the SimpleGIS module:

>>> import SimpleGIS

Now, we can use the now() function to get the current geographic point.

>>> gp = SimpleGIS.GeographicPoint.now()

After we have capture a geographic point, we can call the get_locationInfo() member function to receive the location information.

>>> loc = gp.get_locationInfo()

Now, we can access the infomations such as current country, province, and time zone as we want!

>>> print loc.get_timeZone()
Pacific
>>> print loc.get_city()
Burnaby

Construct a track as you walk
-----------------------------
Now, let's do something more interesting with SimpleGIS. We can construct a movement track using SimpleGIS.

We first construct a Track object to store our geographic points

>>> import SimpleGIS
>>> l = []
>>> t = Track(l)

Now, we can record my geography point every 5 seconds. The following block of code will record the geographic location each 5 seconds for a minutes.

>>> for i in range(12):
>>> 	t.push_back(SimpleGIS.GeographicPoint.now())
>>> 	sleep(5)
>>>

After we have a track, we can use the get_totalDistance() method to measure how far the user have walk so far in kilomiters.

>>> t.get_totalDistance()
0.5

Parse a GPX file in to GeoJson string
-------------------------------------
Let's try importing a GPX file and use our SimpleGIS module to convert it into GeoJson string.

We start by opening  a GPX file and pass it to the GPXFparser using the parse() method.

>>> f = open("foo.gpx", "r")
>>> parser = GPXFParser()
>>> parser.parse()

We have successfully parse the GPX file! Let's convert it into a GeoJson format string.

>>> s = parser.get_GeoJsonFormat()

Finally, we have stroed the Geojson string in the variable s. Let's print it and see how the string looks like.

>>> print s
{"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-122.92156219482422,49.27654080832181]}},{"type":"Feature","properties":{},"geometry":{"type":"Polygon","coordinates":[[[-122.93460845947266,49.28325995376115],[-122.90096282958983,49.283035996995174],[-122.90096282958983,49.269820747425406],[-122.93289184570312,49.27049279471154],[-122.93460845947266,49.28325995376115]]]}}]}


Look inside SimpleGIS
---------------------
If you want to know all the avaliable methods and classes in SimpleGIS, check out our :doc:`API Reference`!