import json
import sys
from subprocess import check_call, check_output, STDOUT

import allure
import requests

@allure.step('Run command "{0}"')
def execute_command(command):
    print command
    sys.stdout.flush()
    return check_call("yes | {0}".format(command), stdout=sys.stdout, stderr=sys.stdout, shell=True)

@allure.step('Run command "{0}"')
def check_command_output(command):
    print command
    sys.stdout.flush()
    return check_output("yes | {0}".format(command), stderr=STDOUT, shell=True)

def allure_attach_json(json_to_attach, message):
    pretty_json = json.dumps(json_to_attach, ensure_ascii=False, indent=4, sort_keys=True)
    allure.attach(message, pretty_json, type=allure.attach_type.JSON)


def make_request(method, url, headers=None, params=None, data=None, json=None, auth=None, timeout=None, verify=False,
                 return_text=None, return_code=None):
    print "### Using url: " + url + " ###################"
    session = requests.Session()
    response = session.request(
        method,
        url,
        headers=headers,
        data=data,
        json=json,
        params=params,
        auth=auth,
        timeout=timeout,
        verify=verify
    )
    if not return_code:
        response.raise_for_status()

    if return_text:
        print "-----------------RESPONSE-----------------------\n"
        print response.text
        return response.text
    elif return_code:
        print "-----------------RESPONSE-----------------------\n"
        print response.status_code
        return response.status_code
    else:
        print "-----------------RESPONSE-----------------------\n"
        print response.json()
        return response.json()