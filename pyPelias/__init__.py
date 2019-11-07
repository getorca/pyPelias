import requests


class pyPelias:
    def __init__(self, http_url):
        self.http_url = http_url

    def geocode(self, query_string):
        r = requests.get(self.http_url + '/v1/search?text='+query_string)
        json = r.json()
        try:
            loc = json['features'][0]['geometry']['coordinates']
            return json
        except IndexError:
            raise Exception('could not parse location text')

    def reverse(self, lat_long):
        r = requests.get(self.http_url + '/v1/reverse?point.lon='+lat_long[1]+'&point.lat='+lat_long[0])

        return r.json()