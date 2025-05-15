from tests.fixtures import station_sample
from src.station    import Station

# -- 4a) -----------------------------------------------------------------------

def test_station_eq_same_code(station_sample: Station):
    same = Station(
        code        = '001', 
        intern_code = 'XYZ', 
        name        = 'Name',
        old_code    = None,
        launch      = None,
        close       = None, 
        st_type     = 'Type',
        area        = 'Area', 
        kind        = 'Kind', 
        voiv        = 'Voiv', 
        city        = 'City', 
        addr        = 'Addr', 
        lat         = 0, 
        lon         = 0
    )
    assert station_sample == same


def test_station_eq_diff_code(station_sample: Station):
    diff = Station(
        code        = '002', 
        intern_code = 'XYZ', 
        name        = 'Name',
        old_code    = None,
        launch      = None,
        close       = None, 
        st_type     = 'Type',
        area        = 'Area', 
        kind        = 'Kind', 
        voiv        = 'Voiv', 
        city        = 'City', 
        addr        = 'Addr', 
        lat         = 0, 
        lon         = 0
    )
    assert station_sample != diff