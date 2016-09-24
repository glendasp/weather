class DummyAPI:
    """This class emulates a weather API."""
    def __init__(self):
        # Pretend data to substitute API calls.
        self._database = {
            '12345': '75F',
            '55555': '0F',
        }

    def current_temp(self, zip_code):
        # Pretend that we are making a request for the current temperature
        # to a weather API here and returning the current temperature.
        return self._database.get(zip_code, None)
