import requests
import configparser

config = configparser.ConfigParser()
config.read("/etc/credentials.conf")
api_key = config.get("configuration", "api_key")


class WPTApi(object):
    def __init__(self):
        self._url_prefix = "http://www.webpagetest.org/k={0}".format(api_key)
        self._request_headers = {}

    def submit_test(self, url, runs, ):
        try:
            r = requests.post("/runtest.php?url={0}&runs=2&f=xml&r=12345".format(url))
        except requests.ConnectionError as e:
            raise WPTException("Unable to connect to WPT Rest API! Error: {0}".format(e), r.status_code)

        return {"status_code": r.status_code, "response": r.content}

    def get_task_status(self, test_id):
        try:
            r = requests.post("/testStatus.php?f=xml&test={0}".format(test_id))
        except requests.ConnectionError as e:
            raise WPTException("Unable to connect to WPT Rest API! Error: {0}".format(e), r.status_code)

        return {"status_code": r.status_code, "response": r.content}

    def get_test_results(self, result_url):
        try:
            r = requests.post(result_url)
        except requests.ConnectionError as e:
            raise WPTException("Unable to connect to WPT Rest API! Error: {0}".format(e), r.status_code)

        return {"status_code": r.status_code, "response": r.content}


class WPTException(Exception):
    def __init__(self, reason, status_code):
        print(str(reason) + '| Status code: ' + str(status_code))
        msg = "Error with status code: %s | Reason: %s" % (str(status_code), str(reason))
        raise Exception(msg)
