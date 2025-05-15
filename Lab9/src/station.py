from typing import Any, Optional


class Station:
    '''Class representing station's data based on 'stacje.csv' file.'''

    def __init__(
            self, code : str, intern_code : str,
            name : str, old_code : Optional[str], launch : Optional[str], 
            close : Optional[str], st_type : str, area : str, kind : str, 
            voiv : str, city : str, addr : str, 
            lat : float, lon : float
        ) -> None:
        self.code : str               = code
        self.intern_code : str        = intern_code
        self.name : str               = name
        self.old_code : Optional[str] = old_code
        self.launch : Optional[str]   = launch
        self.close : Optional[str]    = close
        self.st_type : str            = st_type
        self.area : str               = area
        self.kind : str               = kind
        self.voiv : str               = voiv
        self.city : str               = city
        self.addr : str               = addr
        self.lat : float              = lat
        self.lon : float              = lon



    def __str__(self) -> str:
        return (
            f"'code':               {self.code}\n"
            f"'international_code': {self.intern_code}\n"
            f"'name':               {self.name}\n"
            f"'old_code':           {self.old_code}\n"
            f"'launch_date':        {self.launch}\n"
            f"'close_date':         {self.close}\n"
            f"'station_type':       {self.st_type}\n"
            f"'area_type':          {self.area}\n"
            f"'station_kind':       {self.kind}\n"
            f"'voivodeship':        {self.voiv}\n"
            f"'city':               {self.city}\n"
            f"'address':            {self.addr}\n"
            f"'latitude':           {self.lat}\n"
            f"'longitude':          {self.lon})"
        )



    def __repr__(self) -> str:
        return (
            "Station("
            f"code=                 {self.code!r}, "
            f"international_code=   {self.intern_code!r}, "
            f"name=                 {self.name!r}, "
            f"old_code=             {self.old_code!r}, "
            f"launch_date=          {self.launch!r}, "
            f"close_date=           {self.close!r}, "
            f"station_type=         {self.st_type!r}, "
            f"area_type=            {self.area!r}, "
            f"station_kind=         {self.kind!r}, "
            f"voivodeship=          {self.voiv!r}, "
            f"city=                 {self.city!r}, "
            f"address=              {self.addr!r}, "
            f"latitude=             {self.lat!r}, "
            f"longitude=            {self.lon!r}"
        )



    def __eq__(self, other : Any) -> bool:
        return isinstance(other, Station) and self.code == other.code