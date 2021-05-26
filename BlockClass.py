#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:01:51 2020

@author: gui
"""
import time
from hashlib import sha256
import json


class Block(object):
    
    def __init__(self, data, index, previousHash , timestamp = str(time.time()) ):
        self.data = data
        self.index = index
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.nonce = 0
        
        self._hash = self.calculateHash()
        
    def mineBlock(self, difficulty):
        while self._hash[0 : difficulty] != "0" * difficulty:
            self.nonce += 1
#            print(self.nonce)
            self._hash = self.calculateHash()   
#            print(self._hash)
        print("Block: " + str(self.index))
        print("Nonce: " + str(self.nonce))
        print("Hash: " + self._hash)
        
        
    def calculateHash(self):
        string = json.dumps(self.data) + str(self.index) + str(self.timestamp) + str(self.previousHash)+ str(self.nonce)
        return sha256(string.encode('utf-8')).hexdigest()
    
    def __str__(self):
        string = "Index: " + str(self.index)   +"\nData: "+ json.dumps(self.data) +  "\nTimestamp: " +   str(self.timestamp) + "\nHash: "+  str(self._hash) + "\npreviousHash: "+  str(self.previousHash)
        return string
    
    def __repr__(self):
        string = "Data: "+ json.dumps(self.data) + "\nIndex: " + str(self.index)   + "\nTimestamp: " +   str(self.timestamp)+ "\nHash: " +   str(self._hash)+ "\npreviousHash: "+  str(self.previousHash)
        return string

if __name__ == "__main__":
    chain = Block("Genesis Block", 0, "0")
    import time
    time.sleep(1) 
    child = Block("Children Block", chain.index+1, chain._hash)
    assert chain.calculateHash() == chain._hash
    assert child.calculateHash() == child._hash
