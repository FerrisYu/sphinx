SimpleGIS API Reference 
=======================

.. module:: SimpleGIS

GeographicPoint
---------------
A GeographicPoint object describes a geographic location using latitude, longitude, and elevation.

.. autosummary::

	GeographicPoint
	GeographicPoint.get_closestPoint
	GeographicPoint.get_distance
	GeographicPoint.get_furthestPoint
	GeographicPoint.get_latitude
	GeographicPoint.get_locationInfo
	GeographicPoint.get_longitude
	GeographicPoint.get_time
	GeographicPoint.now
	GeographicPoint.toString

.. autoclass:: SimpleGIS.GeographicPoint
	:members:

GeographicDistance
------------------
A GeographicDistance object describes the 2D distance between two geographic points.

.. autosummary::

	GeographicDistance
	GeographicDistance.get_directDistance
	GeographicDistance.get_latitude_diff
	GeographicDistance.get_longitude_diff	

.. autoclass:: SimpleGIS.GeographicDistance
	:members:

Polygon
-------
A polygon is an area surroundded by a list of geographic points, which are nodes of a polygon.

.. autosummary::
	Polygon
	Polygon.add
	Polygon.get_GPList
	Polygon.get_GeoJsonFormat
	Polygon.get_area
	Polygon.isValid
	Polygon.is_inbound
	Polygon.next
	Polygon.remove

.. autoclass:: SimpleGIS.Polygon
	:members:

Track
-----
A Track is an ordered list of geographic points. It represense a series of geographic points that are captured in order.

.. autosummary::
	Track
	Track.get_GPList
	Track.get_GeoJsonFormat
	Track.get_endTime
	Track.get_point
	Track.get_startTime
	Track.get_totalDistance
	Track.next
	Track.push_back
	Track.remove

.. autoclass:: SimpleGIS.Track
	:members:

GPXFParser
-------------
A parser class for parsing GPX file. It can parse GPX files into Track, Polygon, and GeoJon types.

.. autosummary::
	GPXFParser
	GPXFParser.get_GPList
	GPXFParser.get_GeoJsonFormat
	GPXFParser.get_Track
	GPXFParser.parse

.. autoclass:: SimpleGIS.GPXFParser
	:members:

LocationInfo
------------
A LocationInfo object contains location information about a geographic point.

.. autosummary::
	LocationInfo
	LocationInfo.get_city
	LocationInfo.get_country
	LocationInfo.get_province
	LocationInfo.get_timeZone


.. autoclass:: SimpleGIS.LocationInfo
	:members:
	
ValueOutOfRangeError 
--------------------
There was an value out of the valid range.

.. autoclass:: SimpleGIS.ValueOutOfRangeError 
	:members:

InvalidFormatError 
--------------------
Input file format invalid.

.. autoclass:: SimpleGIS.InvalidFormatError 
	:members:
