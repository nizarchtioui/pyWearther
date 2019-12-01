import requests,sys
class WeatherManager:
    def __init__(self):
        pass


    @staticmethod
    def get_ip():
        try:
            r = requests.get(url="https://api.ipify.org/?format=json")
            return r.json()["ip"]
        except:
            return ""

    @staticmethod
    def getCountryName(ipadress):
        try:
            r = requests.get(url="https://geo.ipify.org/api/v1?apiKey=at_QDhP7vksUtgDKcqi66kQQus3SH399&ipAddress=%s"%ipadress)
            return r.json()["location"]["city"]
        except:
            pass
    @staticmethod
    def getWeatherByCountry(Query):
        try:

            params = {
            'access_key': '515a9c3aaa321a5f9a05f8903ddc7790',
            'query': Query
            }

            api_result = requests.get('http://api.weatherstack.com/current', params)

            api_response = api_result.json()
            return  api_response['current']['temperature']
        except:
            print(sys.exc_info())
            pass
# ipadress  = WeatherManager.get_ip()
# Query = WeatherManager.getCountryName(ipadress)
# WeatherManager.getWeatherByCountry(Query)