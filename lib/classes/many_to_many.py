class NationalPark:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, "name"):
            self._name = name
        
    def trips(self):
        trips = []
        for trip in Trip.all:
            if trip.national_park == self:
                trips.append(trip)
        return trips
    
    def visitors(self):
        visitors = []
        for trip in Trip.all:
            if trip.national_park == self and not visitors.__contains__(trip.visitor):
                visitors.append(trip.visitor)
        return visitors
    
    def total_visits(self):
        visits = 0
        for trip in Trip.all:
            if trip.national_park == self:
                visits += 1
        return visits
    
    def best_visitor(self):
        # import total_visits_at_park from Visitor
        best_visitor = []
        most_visits = 0
        for visitor in Visitor.all:
            visits = visitor.total_visits_at_park(self)
            if visits > most_visits:
                most_visits = visits
                best_visitor = visitor
        return best_visitor


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self._start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date


class Visitor:

    all = []

    def __init__(self, name):
        self._name = name
        Visitor.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        
    def trips(self):
        trips = []
        for trip in Trip.all:
            if trip.visitor == self:
                trips.append(trip)
        return trips
    
    def national_parks(self):
        national_parks = []
        for trip in Trip.all:
            if trip.visitor == self and not national_parks.__contains__(trip.national_park):
                national_parks.append(trip.national_park)
        return national_parks
    
    def total_visits_at_park(self, park):
        visits = 0
        for trip in Trip.all:
            if trip.national_park == park and trip.visitor == self:
                visits += 1
        return visits