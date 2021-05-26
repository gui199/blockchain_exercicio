#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:39:42 2020

@author: gui
"""
from hashlib import sha256

difficulty = 5
nonce = 0
hash_ = "0"
zero = "0"

def mineBlock():
    global hash_
    global nonce
    while hash_[0: difficulty] != zero*difficulty:
        nonce += 1
        print(nonce)
        hash_ = calculateHash()

    print("Nonce: " + str(nonce))
    print("Hash: " + hash_)
        
        
def calculateHash():
    return sha256("Blockchain".encode('utf-8') + str(nonce).encode('utf-8')).hexdigest()

if __name__ == "__main__":
    mineBlock()
    
