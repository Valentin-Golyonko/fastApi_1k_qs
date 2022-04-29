"""
site: https://locust.io/
git: https://github.com/locustio/locust
doc: http://docs.locust.io/en/stable/

Before run:
    - pip install locust gunicorn
    - gunicorn main:fastapi_app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

run:
    locust
"""
import logging

from locust import HttpUser, task
from requests import Response
from requests.exceptions import JSONDecodeError

logger = logging.getLogger(__name__)


class LocustRPS(HttpUser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_start(self):
        pass

    @task
    def endpoints_test(self) -> None:
        # self.endpoint_v1()
        self.endpoint_debug_v1()
        # self.endpoint_debug_v3()
        return None

    """ ------------------ requests methods -> ------------------ """

    def endpoint_v1(self) -> None:
        self.client.get(url="/v1/")
        return None

    def endpoint_debug_v1(self) -> None:
        self.client.get(url="/debug_v1/")
        return None

    def endpoint_debug_v3(self) -> None:
        self.client.get(url="/debug_v3/")
        return None

    """ ------------------ <- requests methods ------------------ """

    """ ------------------ request utilities -> ------------------ """

    @classmethod
    def try_not_200(cls, response: Response) -> None:
        if response.status_code == 0:
            return None
        try:
            response_data = cls.response_json(response)
        except ValueError:
            logger.error(f"try_not_200(): Response content is not valid JSON")
        else:
            logger.info(f"try_not_200(): response detail;"
                        f" detail = {response_data.get('detail')}")
        return None

    @staticmethod
    def response_json(response: Response) -> dict:
        try:
            return response.json()
        except JSONDecodeError as ex:
            logger.error(f"response_json(): JSONDecodeError;"
                         f" {response.url = };"
                         f" {ex.args[0] = }")
        except Exception as ex:
            logger.exception(f"response_json(): response.json() Ex;"
                             f" {response.url = };"
                             f" {ex.args[0] = }")
        return {}

    """ ------------------ <- request utilities ------------------ """
