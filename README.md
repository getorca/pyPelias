# PyPelias - Geocoding and reverse geocoding with Pelias and Python

## Project Description
After installing a planet build of Pelias PyGeo was returning endless errors, It was quicker for me to write this little python API wrapper than try and sort out what the issues where with PyGeo.

This package support geocoding and reverse geo coding to you're own Pelias server using requests and the Pelias API.

## Requirements
A complete install of Pelias. I recommend the Docker env (https://github.com/pelias/docker).


## Installation
install from https://pypi.org/project/pyPelias/

pip install pyPelias

## Usage
```python
import pyPelias

gisAPI = pyPelias('https://mydomain_or_IP_of_pelias')

# reverse geocode - get the location from lat long, in format ['lat', 'long']
loc = gisAPI.reverse(['45.533467', '-122.650095'])

print(loc)

# geocode - takes address, city, state, country in any form, raises exception if can't parse address
geocode = gisAPI.geocode('Alamogordo, New Mexico, United States')

print(geocode)
```

## Notes
We welcome your feedback and support, raise github ticket if you want to report a bug. Need new features? Contact us on github