import logging
import requests

logger = logging.getLogger(__name__)

def extract_weather_data(configs,secrets):
    try:
        # Get the current date and time in UTC
        url = f'{configs["api"]["url"]}?q={configs["api"]["query"]}&appid={secrets["api"]["appid"]}'
        # response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Curitiba&appid=f3946380ac1a5d7f63b058adb10d0387")
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        logger.info('###################################################')
        logger.info(response)
        logger.info('###################################################')
        
        data = response.json()
        logger.info(data)
        return data

    except requests.exceptions.RequestException as e:
        logger.info(f"Request error: {e}")
        return None

    except requests.exceptions.HTTPError as e:
        logger.info(f"HTTP error: {e}")
        return None

    except requests.exceptions.ConnectionError as e:
        logger.info(f"Connection error: {e}")
        return None

    except requests.exceptions.Timeout as e:
        logger.info(f"Timeout error: {e}")
        return None

    except ValueError as e:
        logger.info(f"JSON decode error: {e}")
        return None

    except Exception as e:
        logger.info(f"An unexpected error occurred: {e}")
        return None


