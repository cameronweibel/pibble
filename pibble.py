__author__ = 'Cameron Weibel'

import requests
import json
import RPi.GPIO as GPIO

class Fragment:
    # Creates a knowledge base from local .rubble file on the Rubble web server
    def create_kbase(filename, api_key, api_pass):
        # Reads data from .rubble file
        d = open(filename, 'r').read()
        # URL for API put request
        # File is located at 'file:://domains/USER/filename.rubble'
        url = "https://rubble-beta.viditeck.com/rubble/service/file/domains/cameron/%s" % filename
        try:
            # Put request to store file on the Rubble web server
            put = requests.put(url, data=d, auth=(api_key, api_pass), headers={"content-type": "application/octet-stream"})
        except:
            return "There was an error connecting to the Rubble server"
        # Expects HTTP status code 201
        if put.status
            _code != 201:
            return "Unexpected HTTP status: %d" % put.status_code
        # Returns server response
        data = json.loads(put.content)
        return data['output'][0]


    def spawn_father_process():
        # Create process
        rulesref = "{'rulesref': 'file://domains/cameron/willitcreate,rubble'}"
        url = 'https://rubble-beta.viditeck.com/rubble/service/processcreate'
        try:
            post = requests.post(url, data=rulesref, auth=('uABY0Pf8htbo', 'zLXknuvGra4eNOMX'),
                                 headers={"content-type": "application/json"})
        except:
            return "There was an error connecting to the Rubble server"
        if post.status_code != 200:
            return "Unexpected HTTP status: %d" % post.status_code
        data = json.loads(post.content)
        return data


    # Setup and output 0 or 1 to pins on Raspberry Pi
    def pin_out():
        pinset = []
        for i in pinset:
            if kwargs[pin] == 0:
                GPIO.setup(pin, GPIO.IN)
            if kwargs[pin] == 1:
                GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, kwargs[pin])

    def listener(self):
        while True:
            try:
                response = self.transact()
            except: pass
            try:
                print response['output']
            except:
                print response['error']
            GPIO.output(response['output'])
            self.pinstate = response['output']
            sleep(2)


    def transact(self):
        #data = '[hello_rubble]'
        URL_base = "https://rubble-beta.viditeck.com"
        URL_rest = "/rubble/service/call?wrap-input-from=default&channel=pid(%d)" % self.PID
        URL = URL_base + URL_rest
        try:
            post = requests.post(URL, data=self.data, auth=(self.API_KEY, self.PASS))
        except Exception as e:
            return "There was an error connecting to the Rubble server", e
        if post.status_code != 200:
            return "Unexpected HTTP status: %d" % post.status_code
        data = json.loads(post.content)
            #return data['error']
        return data


create_kbase('test_rules.rubble', 'uABY0Pf8htbo', 'zLXknuvGra4eNOMX')