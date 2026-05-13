import logging

import requests


# Basic HTTP exception
class HTTPStatusException(Exception):
    pass


# Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def request(url: str) -> requests.Response:
    response = requests.get(url, allow_redirects=False)
    status = response.status_code
    if status < 400:
        logging.info(f"Success response, status code: {status}")
        return response
    else:
        raise HTTPStatusException(f"Received an error status code: {status}")


def main():
    base_url = "https://tools-httpstatus.pickup-services.com"

    endpoints = ["/101", "/200", "/301", "/408", "/502"]
    for endpoint in endpoints:
        try:
            request(base_url + endpoint)
        except HTTPStatusException as e:
            logging.error(e)
        except requests.exceptions.RequestException as e:
            # Catching network errors
            logging.error(f"Network error on {endpoint}: {e}")


if __name__ == "__main__":
    main()
