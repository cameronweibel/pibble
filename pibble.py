__author__ = 'Cameron Weibel'

import requests
import json
from time import sleep
import os.path
import pickle
# import RPi.GPIO as GPIO


class Fragment:

    def __init__(self, filename, api_key, api_pass):
        self.filename = filename
        self.api_key = api_key
        self.api_pass = api_pass

    # Creates a knowledge base from local .rubble file on the Rubble web server
    def create_kbase(self):
        # Reads data from .rubble file
        d = open(self.filename, 'r').read()
        # URL for API put request
        # File is located at 'file:://domains/USER/filename.rubble'
        url = "https://rubble-beta.viditeck.com/rubble/service/file/~cameron/%s" % self.filename
        try:
            # Put request to store file on the Rubble web server
            put = requests.put(url, data=d, auth=(self.api_key, self.api_pass),
                               headers={"content-type": "application/octet-stream"})
        except:
            return "There was an error connecting to the Rubble server"
        # Expects HTTP status code 201
        if put.status_code != 201:
            return "Unexpected HTTP status: %d" % put.status_code
        # Returns server response
        return put.content


    def spawn_father_process(self):
        # Create process
        rulesref = "{'rulesref': 'file:/%s'}" % self.filename
        url = 'https://rubble-beta.viditeck.com/rubble/service/processcreate'
        try:
            post = requests.post(url, data=rulesref, auth=(self.api_key, self.api_pass),
                                 headers={"content-type": "application/json"})
        except:
            return "There was an error connecting to the Rubble server"
        if post.status_code != 200:
            return "Unexpected HTTP status: %d" % post.status_code
        data = json.loads(post.content)
        self.pid = int(data['pid'])
        outfile = open('pid.txt','wb')
        pickle.dump(self.pid, outfile)
        outfile.close()


    def transact(self):
        message = '[hello_rubble]'
        URL_base = "https://rubble-beta.viditeck.com"
        URL_rest = "/rubble/service/call?wrap-input-from=default&channel=pid(%d)" % self.pid
        URL = URL_base + URL_rest
        try:
            post = requests.post(URL, data=message, auth=(self.api_key, self.api_pass))
        except Exception as e:
            return "There was an error connecting to the Rubble server", e
        if post.status_code != 200:
            print "Unexpected HTTP status: %d" % post.status_code
        data = json.loads(post.content)
        return data

    def listener(self):
        terminate = False
        while not terminate:
            try:
                response = self.transact()
            except:
                pass
            try:
                print response['output']
            except:
                print response['error']
            sleep(2)

if __name__ == "__main__":
    first = Fragment("test_rules.rubble", 'uABY0Pf8htbo', 'zLXknuvGra4eNOMX')

    if not os.path.isfile('pid.txt'):
        print first.create_kbase()
        print first.spawn_father_process()
        print first.pid
    else:
        infile = open('pid.txt','rb')
        first.pid = pickle.load(infile)

    print first.pid
    print first.transact()
    print first.listener()