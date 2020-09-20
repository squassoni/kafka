from klein import run, route
from twisted.internet.defer import succeed
import json
import requests
import logging

@route('/teste', methods=['POST'])
def noi_integration(request):
    #content = json.loads(request.content.read())
    content = request.content.read()    
    #header = request.header.read()

    print(content)
    #print(header)

    return content

@route('/oauth/token')
def noi_integration2(request):

    return True

run("localhost",3003)
