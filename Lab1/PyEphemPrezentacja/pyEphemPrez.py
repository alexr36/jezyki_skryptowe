import ephem

#   Obliczanie wschodu i zachodu Słońca nad Wrocławiem
#   Tworzenie obserwatora
observer = ephem.Observer()
observer.lat, observer.lon = '51.107883', '17.038538'   # Wrocław
observer.date = '2025/03/13'                            # Określona data

#   Obliczanie wschodu i zachodu Słońca
sunrise = observer.next_rising(ephem.Sun())
sunset = observer.next_setting(ephem.Sun())

print(f"Wschod Slonca: {sunrise}")
print(f"Zachod Slonca: {sunset}\n")


#   Obliczanie aktualnej pozycji Słońca

sun = ephem.Sun()
sun.compute()
print(f"Slonce - RA: {sun.ra}, DEC: {sun.dec}\n")


#   Obliczanie fazy Księżyca dla zadanej daty

moon = ephem.Moon()
moon.compute('2025/03/13')
print(f"Faza Ksiezyca: {moon.phase}\n")


#   Obliczanie pozycji planet - Mars

mars = ephem.Mars()
mars.compute()
print(f"Mars - RA: {mars.ra}, DEC: {mars.dec}\n")


#   Obliczanie dla własnych obiektów astronomicznych

my_star = ephem.readdb("MyStar,f|M|F7,10:08:22.3,+11:58:02,2.0,2000")
my_star.compute()
print(f"Moja gwiazda - RA: {my_star.ra}, DEC - {my_star.dec}\n")