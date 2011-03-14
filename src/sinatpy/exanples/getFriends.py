#!/usr/bin/python
#coding=gbk

'''
Created on Aug 2, 2010

@author: ting
'''

import unittest
from weibopy.auth import OAuthHandler, BasicAuthHandler
from weibopy.api import API

class test(unittest.TestCase):
    
    consumer_key= "2967452232"
    consumer_secret ="0fb77c003faf71cc503751829f118057"
    
    def __init__(self):
            """ constructor """
    
    def getAtt(self, key):
        try:
            return self.obj.__getattribute__(key)
        except Exception, e:
            print e
            return ''
        
    def getAttValue(self, obj, key):
        try:
            return obj.__getattribute__(key)
        except Exception, e:
            print e
            return ''
        
    def auth(self):
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth_url = self.auth.get_authorization_url()
        print 'Please authorize: ' + auth_url
        verifier = raw_input('PIN: ').strip()
        self.auth.get_access_token(verifier)
        self.api = API(self.auth)
    def basicAuth(self, source, username, password):
        self.auth = BasicAuthHandler(username, password)
        self.api = API(self.auth,source=source)      
    def setToken(self, token, tokenSecret):
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.setToken(token, tokenSecret)
        self.api = API(self.auth)
        
    def friends(self):
        timeline = self.api.friends()
        for line in timeline:
            self.obj = line
            fid = self.getAtt("id")
            name = self.getAtt("screen_name")
            print "friends---"+ str(fid) +":"+ name



test = test()
#AccessToken的 key和Secret
test.setToken('0f58140e570dcab866a6d892b34b10d5', "c2d600a6836929a9ce82489846caea2e")
test.friends()

