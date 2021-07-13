"""odoo integration module"""

import xmlrpc.client


import xmlrpc.client

url = 'http://52.142.63.20:1269'
db = 'fraccion_test'
username = 'WSadnet@adnetworks.cl'
password = 'WSadnet@adnetworks.cl'

class OdooClient():

   
    def __init__(self):
        self.url = url
        self.db = db
        self.username = username
        self.password = password


    def logging(self):
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        common.version()
        uid = common.authenticate(db, username, password, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        return uid, models