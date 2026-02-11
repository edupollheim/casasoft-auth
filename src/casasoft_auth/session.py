import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def create_session():
    session = requests.Session()

    retries = Retry(
        total=5,
        backoff_factor=1.5,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET", "POST"]
    )

    adapter = HTTPAdapter(max_retries=retries)
    session.mount("https://", adapter)

    return session
