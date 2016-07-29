class LocationInfo(object):
    """
    Construct a locationInfo object.

    :param country(str): country of this new location.
    :param province(str): province of this new location.
    :param city(str): city of this new location.
    :param timeZone(str): timeZone of this new location.

    .. note::

        You shouldn't construct objects of this class yourself, instead, you will get the object from the get_locationInfo method in GeographicPoint class.

    """

    def __init__(self, country,province,city,timeZone):
        """
        """

    def get_country(self):
        """This gets the country of this location

        >>> import SimpleGIS
        >>> loc = SimpleGIS.LocationInfo("Canada","BC","Vancouver", "Pacific")
        >>> print loc.get_country()
        Canada

        """

    def get_province(self):
        """This gets the province of this location

        >>> import SimpleGIS
        >>> loc = SimpleGIS.LocationInfo("Canada","BC","Vancouver", "Pacific")
        >>> print loc.get_province()
        BC

        """

    def get_city(self):
        """This gets the city of this location 

        >>> import SimpleGIS
        >>> loc = SimpleGIS.LocationInfo("Canada","BC","Vancouver", "Pacific")
        >>> print loc.get_city()
        Vancouver

        """

    def get_timeZone(self):
        """This gets the time zone of this location 

        >>> import SimpleGIS
        >>> loc = SimpleGIS.LocationInfo("Canada","BC","Vancouver", "Pacific")
        >>> print loc.get_timeZone()
        Pacific

        """

class GeographicPoint(object):
    """Construct a GeographicPoint object.

    :param latitude(float): latitude of the geographic coordinate. Range: -90 ~ 90.
    :param longitude(float): longitude of the geographic coordinate. Range: -180 ~ 180.
    :param elevation(float): (optional) elevation of the geographic coordinate. None if this is a 2D geographic coordinates.
    :param time(datetime): (optional) The time when the point was recorded. 

    :raises ValueOutOfRangeError: Raise when latitude or longitude is out of range.
    """

    def __init__(self, latitude, longitude, elevation=None, time=None):
        """
        """

    def now():
        """Set this object with the 3D geographic attributes of the current positition, and the time when it's taken.
        
        :rtype: SimpleGIS.GeographicPoint

        >>> import SimpleGIS
        >>> gp = SimpleGIS.GeographicPoint.now()
        >>> loc = gp.get_locationInfo()
        >>> print loc.get_timeZone()
        Pacific

        """

    def get_locationInfo(self):
        """Gets the location information for the current geographic coordinate.

        :rtype: SimpleGIS.LocationInfo

        >>> import SimpleGIS
        >>> gp = SimpleGIS.GeographicPoint.now()
        >>> loc = gp.get_locationInfo()
        >>> print loc.get_timeZone()
        Pacific

        """
        return loc

    def get_latitude(self):
        """Gets the latitude of the current geographic coordinate.

        :rtype: float

        >>> import SimpleGIS
        >>> gp = SimpleGIS.GeographicPoint.now()
        >>> print gp.get_latitude()
        49.246292

        """
        return l

    def get_longitude(self):
        """Gets the longitude of the current geographic coordinate.

        :rtype: float

        >>> import SimpleGIS
        >>> gp = SimpleGIS.GeographicPoint.now()
        >>> print gp.get_longitude()
        -123.116226

        """

        return loc

    def get_time(self):
        """Gets the time when the point was taken.

        :rtype: datetime

        >>> import SimpleGIS
        >>> gp = SimpleGIS.GeographicPoint.now()
        >>> print gp.get_time()
        datetime(2015, 6, 10, 15, 8, 24, 78915)

        """

    def get_furthestPoint(self, gp_list):
        """Gets the furtest GeographicPoint object in a list of GeographicPoint based on their 2D direct distance with the current GeographicPoint.

        :param gp_list(GeographicPoint[]): A list of GeographicPoint used to measure the 2D distance.
        :rtype: SimpleGIS.GeographicPoint

        >>> import SimpleGIS
        >>> l = []
        >>> l.append(SimpleGIS.GeographicPoint(10,20))
        >>> l.append(SimpleGIS.GeographicPoint(0,0))        
        >>> gp = SimpleGIS.GeographicPoint.now()
        >>> fp = gp.get_furthestPoint(l)
        >>> fp.get_latitude()
        0

        """
        return gd

    def get_closestPoint(self, gp_list):
        """Gets the closest GeographicPoint object in a list of GeographicPoint based on their 2D direct distance with the current GeographicPoint.

        :param gp_list(GeographicPoint[]): A list of GeographicPoint used to measure the 2D distance.
        :rtype: SimpleGIS.GeographicPoint

        >>> import SimpleGIS
        >>> l = []
        >>> l.append(SimpleGIS.GeographicPoint(10,20))
        >>> l.append(SimpleGIS.GeographicPoint(0,0))
        >>> gp = SimpleGIS.GeographicPoint(20,40)
        >>> cp = gp.get_closestPoint(l)
        >>> cp.get_latitude()
        10

        """

        return gd

    def get_distance(self, other):
        """Gets the 2D geographic distance between the other and this Geographic Point. 

        .. note::

            Distance is measure in two dimension. 3D geographic points are treated as 2D points.

        :param other(GeographicPoint): The GeographicPoint used to measure the distance.

        :rtype: SimpleGIS.GeographicDistance

        >>> import SimpleGIS
        >>> p1 = SimpleGIS.GeographicPoint(3,4)
        >>> p2 = SimpleGIS.GeographicPoint(0,0)
        >>> gd = p1.get_distance(p2)
        >>> gd.get_direct_distance()
        5
        """
        return gp

    def toString():
        """Return a string of that value it in degrees, minutes, seconds format.

        :rtype: str

        >>> import SimpleGIS
        >>> p1 = SimpleGIS.GeographicPoint(49.276765,-122.917957)
        >>> p1.toString
        49d16m36s N 122d55m4s W         

        """


class GeographicDistance(object):
    """Construct a GeographicDistance object

    :param d_latitude(float): latitude difference between the two geographic points. Range: 0 ~ 180.
    :param d_longitude(float): longitude difference between the two geographic points. Range: 0 ~ 360.

    :raises ValueOutOfRangeError: Raise when latitude or longitude difference is out of range.

    .. note::

        You shouldn't construct objects of this class yourself, instead, you will get the object from the get_distance method in GeographicPoint class.

    """

    def __init__(self, d_latitude, d_longitude):
        """
        """

    def get_latitude_diff(self):
        """Gets the latitude difference between the two geographic points.

        :rtype: float

        >>> import SimpleGIS
        >>> p1 = SimpleGIS.GeographicPoint(3,4)
        >>> p2 = SimpleGIS.GeographicPoint(0,0)
        >>> gd = p1.get_distance(p2)
        >>> gd.get_latitude_diff()
        3

        """
        return

    def get_longitude_diff(self):
        """Gets the longitude difference between the two geographic points.

        :rtype: float

        >>> import SimpleGIS
        >>> p1 = SimpleGIS.GeographicPoint(3,4)
        >>> p2 = SimpleGIS.GeographicPoint(0,0)
        >>> gd = p1.get_distance(p2)
        >>> gd.get_longitude_diff()
        4

        """
        return

    def get_directDistance(self):
        """Gets the direct_distance between the two geographic points in km.

        :rtype: float

        >>> import SimpleGIS
        >>> p1 = SimpleGIS.GeographicPoint(3,4)
        >>> p2 = SimpleGIS.GeographicPoint(0,0)
        >>> gd = p1.get_distance(p2)
        >>> gd.get_direct_distance()
        555.986

        """
        return

class Polygon(object):
    """Construct a Polygon object.

    :param gp_list(GeographicPoint[]): a list of geographic points which represense the nodes of the polygon. 


    """

    def __init__(self, gp_list):
        """
        """

    def isValid():
        """
        Check whether the current gp_list con construct a valid polygon. 

        :rtype: Boolean

        >>> import SimpleGIS
        >>> l = []
        >>> l.append(SimpleGIS.GeographicPoint(3,0))
        >>> l.append(SimpleGIS.GeographicPoint(0,4))
        >>> l.append(SimpleGIS.GeographicPoint(0,0))
        >>> p = Polygon(l)
        >>> p.isValid()
        true
        >>> p.remove(SimpleGIS.GeographicPoint(0,0))
        >>> p.isValid()
        false

        """
    def next(self):
        """
        Return the next geographic point in gp_list. Starts at the first point, and returns None after it reach the last point of the list.

        :rtype: SimpleGIS.GeographicPoint

        """

    def get_GPList(self):
        """Return the stored list of geographic points

        :rtype: list

        >>> import SimpleGIS
        >>> l = []
        >>> l.append(SimpleGIS.GeographicPoint(10,20))
        >>> l.append(SimpleGIS.GeographicPoint(0,0))
        >>> p = Polygon(l)
        >>> l2 = p.get_GPList();
        >>> print l2[0].get_latitude();
        10

        """

    def add(self, gp):
        """Add a new point to the polygon.

        :param gp(GeographicPoint): a geographic point to add to the polygon.

        >>> import SimpleGIS
        >>> l = []
        >>> l.append(SimpleGIS.GeographicPoint(3,0))
        >>> l.append(SimpleGIS.GeographicPoint(0,4))
        >>> p = Polygon(l)
        >>> p.add(SimpleGIS.GeographicPoint(0,0))
        >>> p.get_area()
        6

        """

    def remove(self, i):
        """Remove a point from the polygon

        :param i(int): the index of the geographic point to remove.

        >>> import SimpleGIS
        >>> l = []
        >>> l.append(SimpleGIS.GeographicPoint(3,0))
        >>> l.append(SimpleGIS.GeographicPoint(0,4))
        >>> l.append(SimpleGIS.GeographicPoint(0,0))
        >>> p = Polygon(l)
        >>> p.remove(0)
        >>> p.get_area()
        -1

        """

    def is_inbound(gp):
        """Returns true if the geographic point is inside or on edge of the polygon, false if not.
        
        :param gp(GeographicPoint): a geographic point to check whether is inbound.
        
        :rtype: Boolean

        >>> import SimpleGIS
        >>> l = []
        >>> l.append(SimpleGIS.GeographicPoint(3,0))
        >>> l.append(SimpleGIS.GeographicPoint(0,4))
        >>> l.append(SimpleGIS.GeographicPoint(0,0))
        >>> p = Polygon(l)
        >>> gp = SimpleGIS.GeographicPoint(1,1)
        >>> p.is_inbound(gp)
        True

        """

    def get_area():
        """Return the area of the polygon.
    
        >>> import SimpleGIS
        >>> l = []
        >>> l.append(SimpleGIS.GeographicPoint(3,0))
        >>> l.append(SimpleGIS.GeographicPoint(0,4))
        >>> l.append(SimpleGIS.GeographicPoint(0,0))
        >>> p = Polygon(l)
        >>> p.get_area()
        6
        >>> p.remove(SimpleGIS.GeographicPoint(0,0))
        >>> p.get_area()
        -1

        .. note::

            At least 3 geographic points are needed to get a polygon area. Polygon with least than 3 geographic points will return -1.

        """

    def get_GeoJsonFormat(self):
        """Convert a polygon object to a valid GeoJson string. GeoJon format is a valid format to export to google map.

        :rtype: str

        >>> import SimpleGIS
        >>> l = []
        >>> l.append(SimpleGIS.GeographicPoint(3,0,0,datetime.datetime.now()))
        >>> l.append(SimpleGIS.GeographicPoint(0,4,0,datetime.datetime.now()))
        >>> l.append(SimpleGIS.GeographicPoint(0,0,0,datetime.datetime.now()))
        >>> p = Polygon(l) 
        >>> s = p.get_GeoJsonFormat()
        >>> print s
        {"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-122.92156219482422,49.27654080832181]}},{"type":"Feature","properties":{},"geometry":{"type":"Polygon","coordinates":[[[-122.93460845947266,49.28325995376115],[-122.90096282958983,49.283035996995174],[-122.90096282958983,49.269820747425406],[-122.93289184570312,49.27049279471154],[-122.93460845947266,49.28325995376115]]]}}]}

        """

class Track(object):
    """Construct a Track object.

    :param gp_list(GeographicDistance[]): a ordered list of 3D geographic points with recorded time.

    """
    
    def __init__(self, gp_list):
        """
        """

    def next(self):
        """
        Return the next geographic point in the ordered geographic point list. Starts at the first point, and returns None after it reach the last point of the list.

        :rtype: SimpleGIS.GeographicPoint

        >>> import SimpleGIS
        >>> l = []
        >>> l.append(SimpleGIS.GeographicPoint(10,20,0,datetime.datetime.now()))
        >>> l.append(SimpleGIS.GeographicPoint(0,0,0,datetime.datetime.now()))
        >>> t = Track(l)
        >>> gp = t.next()
        >>> gp.get_latitude
        10

        """

    def get_GPList(self):
        """Return a list of geographic points
    
        :rtype: list

        >>> import SimpleGIS
        >>> l = []
        >>> l.append(SimpleGIS.GeographicPoint(10,20,0,datetime.datetime.now()))
        >>> l.append(SimpleGIS.GeographicPoint(0,0,0,datetime.datetime.now()))
        >>> t = Track(l)
        >>> l2 = t.get_GPList();
        >>> print l2[0].get_latitude();
        10

        """

    def get_point(self,i):
        """Return the geographic point at index location.

        :param i(int): index of the geographic point to get.

        :rtype: SimpleGIS.GeographicPoint

        >>> import SimpleGIS
        >>> l = []
        >>> l.append(SimpleGIS.GeographicPoint(10,20,0,datetime.datetime.now()))
        >>> l.append(SimpleGIS.GeographicPoint(0,0,0,datetime.datetime.now()))
        >>> t = Track(l)
        >>> gp = t.get_point(0);
        >>> print gp.get_latitude();
        10

        """

    def get_startTime(self):
        """Return the recorded time of the first stored geographic point.
        
        :rtype: datetime

        >>> import SimpleGIS
        >>> l = []
        >>> l.append(SimpleGIS.GeographicPoint(0,0,0,datetime.datetime.now()))
        >>> t = Track(l) 
        >>> t.get_startTime()
        datetime(2015, 6, 10, 15, 8, 24, 78915)

        """

    def get_endTime(self):
        """Return the recorded time of the last stored geographic point.

        :rtype: datetime

        >>> import SimpleGIS
        >>> l = []
        >>> l.append(SimpleGIS.GeographicPoint(0,0,0,datetime.datetime.now()))
        >>> t = Track(l) 
        >>> t.get_endTime()
        datetime(2015, 6, 10, 15, 8, 24, 78915)

        """

    def get_totalDistance(self):
        """Return the total distance traveled of the track in km . Evaluate from distances between each adjacent point.

        :rtype: float 

        >>> import SimpleGIS
        >>> l = []
        >>> l.append(SimpleGIS.GeographicPoint(3,0,0,datetime.datetime.now()))
        >>> l.append(SimpleGIS.GeographicPoint(0,4,0,datetime.datetime.now()))
        >>> t = Track(l) 
        >>> t.get_totalDistance()
        555.986

        """

    def get_GeoJsonFormat(self):
        """Convert a track object to a valid GeoJson string. GeoJon format is a valid format to export to google map.

        :rtype: str

        >>> import SimpleGIS
        >>> l = []
        >>> l.append(SimpleGIS.GeographicPoint(3,0,0,datetime.datetime.now()))
        >>> l.append(SimpleGIS.GeographicPoint(0,4,0,datetime.datetime.now()))
        >>> t = Track(l)    
        >>> s = t.get_GeoJsonFormat()
        >>> print s
        {"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-122.92156219482422,49.27654080832181]}},{"type":"Feature","properties":{},"geometry":{"type":"Polygon","coordinates":[[[-122.93460845947266,49.28325995376115],[-122.90096282958983,49.283035996995174],[-122.90096282958983,49.269820747425406],[-122.93289184570312,49.27049279471154],[-122.93460845947266,49.28325995376115]]]}}]}

        """

    def push_back(self, gp):
        """Add a new point to the end of the ordered list.

        :param gp: a geographic point to add to the back of the track.
        :type gp: GeographicPoint

        >>> import SimpleGIS
        >>> l = []
        >>> l.append(SimpleGIS.GeographicPoint(3,0,0,datetime.datetime.now()))
        >>> t = Track()
        >>> t.push_back(SimpleGIS.GeographicPoint(0,4,0,datetime.datetime.now()))
        >>> t.get_totalDistance()
        555.986

        """

    def remove(self, i):
        """Remove a point from the polygon

        :param i(int): the index of the geographic point to remove.

        >>> import SimpleGIS
        >>> l = []
        >>> l.append(SimpleGIS.GeographicPoint(0,0,0,datetime.datetime.now()))
        >>> l.append(SimpleGIS.GeographicPoint(3,0,0,datetime.datetime.now()))
        >>> l.append(SimpleGIS.GeographicPoint(0,4,0,datetime.datetime.now()))
        >>> t = Track(l)
        >>> t.remove(0)
        >>> t.get_totalDistance()
        555.986

        """


class GPXFParser(object):
    """
    Construct a GPXFParser object.
    """
    def __init__(self, gpx_f):
        """
        """

    def parse(self, gpx_f):
        """Parse the input GPX file. Throws InvalidFormatError error if file is not valid GPX file.

        :param gpx_f(File): An readable opened file with suffix .gpx.

        :raises InvalidFormatError: Raise when the input format is not valid .gpx file.

        >>> f = open("foo.gpx", "r")
        >>> parser = GPXFParser()
        >>> parser.parse()


        """

    def get_Track(self):
        """Parse a valid GPX into a Track object.

        :rtype: SimpleGIS.Track

        >>> import SimpleGIS
        >>> f = open("foo.gpx", "r")
        >>> parser = GPXFParser()
        >>> parser.parse()
        >>> t = parser.get_Track()
        >>> t.get_startTime()
        datetime(2015, 6, 10, 15, 8, 24, 78915)

        """

    def get_GPList(self):
        """Parse a valid GPX into a list of geographic points.

        :rtype: list

        >>> import SimpleGIS
        >>> f = open("foo.gpx", "r")
        >>> parser = GPXFParser()
        >>> parser.parse()
        >>> gp_list = parser.get_GPList()
        >>> gp_list[0].get_time()
        datetime(2015, 6, 10, 15, 8, 24, 78915)

        """

    def get_GeoJsonFormat(self):
        """Parse a valid GPX into a valid GeoJson string. GeoJon format is a valid format to export to google map.

        :rtype: str

        >>> import SimpleGIS
        >>> f = open("foo.gpx", "r")
        >>> parser = GPXFParser()
        >>> parser.parse()
        >>> s = parser.get_GeoJsonFormat()
        >>> print s
        {"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-122.92156219482422,49.27654080832181]}},{"type":"Feature","properties":{},"geometry":{"type":"Polygon","coordinates":[[[-122.93460845947266,49.28325995376115],[-122.90096282958983,49.283035996995174],[-122.90096282958983,49.269820747425406],[-122.93289184570312,49.27049279471154],[-122.93460845947266,49.28325995376115]]]}}]}

        """


class ValueOutOfRangeError (IOError):
    """
    """

    def __init__(self):
        """
        """

    def toString():
        """Print out error message. 

        :rtype: str


        """


class InvalidFormatError (IOError):
    """
    """

    def __init__(self):
        """
        """

    def toString():
        """Print out error message. 

        :rtype: str


        """

