import pycountry
class CountriesManger:
    def __init__(self):
        pass
    @staticmethod
    def getSuggsetions():
        try:
           r =  pycountry.countries.lookup('usa')
           print(r)
        except:
            pass

CountriesManger.getSuggsetions()