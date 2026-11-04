import math, pprint

class EventManager:
    EARTH_RADIUS = 6378100     # radius of the earth in m

    def __init__(self, eventList):
        self.eventList = eventList

    def distance(self, lat1, lon1, lat2, lon2):
        # https://stackoverflow.com/a/27943

        dLat = self.deg2rad(lat2 - lat1)
        dLon = self.deg2rad(lon2 - lon1)
        a = math.sin(dLat / 2) * math.sin(dLat / 2) + \
            math.cos(self.deg2rad(lat1)) * math.cos(self.deg2rad(lat2)) * \
            math.sin(dLon / 2) * math.sin(dLon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));
        return self.EARTH_RADIUS * c    # distance in m

    def deg2rad(self, d):
        return d * math.pi / 180

    def findEventsNear(self, lat, lon, maxDist=5000):
        events = []

        for event in self.eventList:
            name, type, elat, elon, _ = event.split(":")
            elat = float(elat)
            elon = float(elon)

            if self.distance(lat, lon, elat, elon) < maxDist:
                events.append(event)

        return events

    def findEarthquakesNear(self, cityName):
        cityRecord = None

        for event in self.eventList:
            if event is City and name == cityName:
                cityRecord = event

        if cityRecord is None:
            return None

        clat = float(clat)
        clon = float(clon)

        events = []

        for event in self.eventList:
            name, type, elat, elon, _ = event.split(":")
            elat = float(elat)
            elon = float(elon)

            if type == "earthquake":
                if self.distance(elat, elon, clat, clon) < 5000:
                    events.append(event)

        return events


    def addEvent(self, name, lat, lon, type, time=-1):
        self.eventList.append(Event(name, type, lat, lon, time))

class Event:
    def __init__(self, name, type, lat, lon, time=-1):
        self.name = name
        self.type = type
        self.lat = lat
        self.lon = lon
        self.time = time

class City(Event):
    def __init__(self, name, lat, lon):
        super.__init__(name, "city", lat, lon, -1)

    


starting_events = [
    "some volcano:volcano:40.12120:-121.3455:21451",
    "some earthquake:earthquake:40.51230:-121.23425:87153",
    "another earthquake:earthquake:39.23890:-120.23985:17354",
    "yet another earthquake:earthquake:39.23223:-120.23125:16524",
    "another volcano:volcano:43.32890:-122.3289:23856",
    "a geyser:geyser:39.23223:-120.23125:-1",
    "Townville:city:44.05645:-121.30812:-1"
]

em = EventManager(starting_events)

em.addEvent("my favorite hotspring", 46.1231, -115.23234, "hotspring")
em.addEvent("Cityton", 40.5232, -121.23453, "city")
em.addEvent("yet another volcano", 15.52232, -107.03521, "volcano", 256923)

x = em.findEventsNear(40.5, -121.2, 163000)
pprint.pprint(x)

print("------------------------")

x = em.findEarthquakesNear("Cityton")
pprint.pprint(x)