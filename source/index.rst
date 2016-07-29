.. rough documentation master file, created by
   sphinx-quickstart on Sat Jun 18 16:14:57 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to SimpleGIS!
=================================

SimpleGIS is a geographic information systems library written in Python. It abstracts the complex geographic data types into three simple classes, GeographicPoint, Polygon, and Track. These class are all Google Map portable. They can be converted into GeoJson format, and then export to Google Map for display purpose.

SimpleGIS also provides a GPXFParser class for importing GPX files. GPX is a common GPS data format, and GPX files can be converted into a track objects as well as a list of GeographicPoints.

Check out our :doc:`tutorials` guide if you are new to SimpleGIS. You can also find every detail of the library in :doc:`API Reference`.

.. toctree::
   :maxdepth: 2

   tutorials

   API Reference

Index
=====

* :ref:`genindex`

