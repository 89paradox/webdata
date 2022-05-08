import requests
import os
def get_response(web_url):
    try:
        response = requests.get(web_url)
    except:
        raise Exception("Error while getting response, is the URL correct?")
    finally:
        return response.content
def up_chk(web_url):
    try:
        requests.get(web_url, stream = True)
    except:
        return False
    finally:
        return True
