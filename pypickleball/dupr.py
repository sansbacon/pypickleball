# dupr.py
# DUPR-related classes

from time import sleep
import requests


class DUPRClient:
    """Class to access DUPR API"""

    API_URL = 'https://api.dupr.gg/player/v1.0/search'

    def __init__(self, access_token: str, delay: float = 1.0):
        self.access_token = access_token
        self.session = requests.Session()
        self.delay = delay

    @property
    def headers(self):
        return {
            'authority': 'api.dupr.gg',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'authorization': f'Bearer {self.access_token}',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://mydupr.com',
            'referer': 'https://mydupr.com/',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'x-access-token': self.access_token
        }

    @staticmethod
    def post_body(limit: int = 10, offset: int = 0, query: str = '*', exclude: list = None, include_unclaimed: bool = True, filter: dict = None, **kwargs):
        """Creates body for POST request"""
        return {
          'limit': str(limit),
          'offset': str(offset),
          'query': query,
          'exclude': exclude if exclude else [],
          'includeUnclaimedPlayers': include_unclaimed,
          'filter': filter
        }

    @staticmethod
    def rating_filter(**kwargs):
        """Generates rating filter from component parts"""
        return {
          'type': kwargs.get('rating_type', 'DOUBLES'),
          'minRating': str(kwargs.get('min_rating', 2.0)),
          'maxRating': str(kwargs.get('max_rating', 8.0))
        }

    @staticmethod
    def search_filters(lat: float = 41.8850, lng: float = -87.7845, rating: dict = None, gender: str = None, radius: int = 80467):
        """Generates search filters"""
        d = {}
        if lat:
            d['lat'] = lat
        if lng:
            d['lng'] = lng
        if rating:
            d['rating'] = rating
        if gender:
            d['gender'] = gender
        if radius:
            d['radiusInMeters'] = radius
        return d

    def query(self, **kwargs):
        """Query API"""
        # step one: build rating filter
        rating = self.rating_filter(**kwargs)
        return rating
        #json_data = self.post_body(**kwargs)
        #r = self.session.post(self.API_URL, headers=self.headers, json=json_data)
        #if self.dely:
        #    sleep(self.delay)


if __name__ == '__main__':
    pass
    #c = DUPRClient(access_token=None)
    #print(c.query(a=1, b=2))