class Station:
    '''Class representing station's data based on 'stacje.csv' file.'''

    def __init__(
            self, code, intern_code,
            name, old_code, launch, 
            close, type, area, kind, 
            voiv, city, addr, 
            lat, lon
        ):
        self.code = code
        self.intern_code = intern_code
        self.name = name
        self.old_code = old_code
        self.launch = launch
        self.close = close
        self.type = type
        self.area = area
        self.kind = kind
        self.voiv = voiv
        self.city = city
        self.addr = addr
        self.lat = lat
        self.lon = lon



    def __str__(self):
        return (
            f"'code':               {self.code}\n"
            f"'international_code': {self.intern_code}\n"
            f"'name':               {self.name}\n"
            f"'old_code':           {self.old_code}\n"
            f"'launch_date':        {self.launch}\n"
            f"'close_date':         {self.close}\n"
            f"'station_type':       {self.type}\n"
            f"'area_type':          {self.area}\n"
            f"'station_kind':       {self.kind}\n"
            f"'voivodeship':        {self.voiv}\n"
            f"'city':               {self.city}\n"
            f"'address':            {self.addr}\n"
            f"'latitude':           {self.lat}\n"
            f"'longitude':          {self.lon})"
        )



    def __repr__(self):
        return (
            "Station("
            f"code=                 {self.code!r}, "
            f"international_code=   {self.intern_code!r}, "
            f"name=                 {self.name!r}, "
            f"old_code=             {self.old_code!r}, "
            f"launch_date=          {self.launch!r}, "
            f"close_date=           {self.close!r}, "
            f"station_type=         {self.type!r}, "
            f"area_type=            {self.area!r}, "
            f"station_kind=         {self.kind!r}, "
            f"voivodeship=          {self.voiv!r}, "
            f"city=                 {self.city!r}, "
            f"address=              {self.addr!r}, "
            f"latitude=             {self.lat!r}, "
            f"longitude=            {self.lon!r}"
        )



    def __eq__(self, other):
        return isinstance(other, Station) and self.code == other.code