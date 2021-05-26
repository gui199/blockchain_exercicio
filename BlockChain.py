#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:59:17 2020

@author: gui
"""

from BlockClass import Block

class BlockChain(object):
    def __init__(self):
        self.chain = [self.createGenesisBlock() ]
        self.difficulty = 5
     
    def createGenesisBlock(self):
        genesisDate = 930798000 #"01/07/1999"        
        return  Block("Genesis Block", 0, "0",  genesisDate)
    
    def getLastBlock(self):
#        return self.chain[len(self.chain) - 1]
        return  len(self.chain) - 1
    
    def addNewBlock(self, newBlock):
        newBlock.previousHash = self.chain[self.getLastBlock()]._hash
        newBlock.index = self.getLastBlock() + 1        
        newBlock._hash = newBlock.calculateHash()
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock) 
        
    def isChainValid(self):
        chain = self.chain        
        for i in range(self.getLastBlock()+1):
            print(i)
            if chain[i]._hash != chain[i].calculateHash():
                print(i)
                print("hash: "+ chain[i]._hash)
                print("calculateHash(): "+ chain[i].calculateHash())
                print("Block "+str( i)+" has been corrupted!")
                
            elif i > 0 and chain[i].previousHash != chain[i-1]._hash:
                print("Block "+str( i-1)+" has been corrupted")
            
            else:
                print("Chain is Valid.")
        
    def __str__(self):
        string =  "Lenght: "+ str(len(PolyChain.chain)) 
        return string
    
    def __repr__(self):
        string = self.chain.__repr__()
        return string

if __name__ == "__main__":
    blockToAdd = 5
    PolyChain = BlockChain()
    for i in range(blockToAdd):
        PolyChain.addNewBlock( Block (
                {"sender": "Polycode",
                 "receiver": "Youtube",
                 "message": "Block "+ str( len(PolyChain.chain) ) +" has been added to the chain."
                 } , 0   , 0  ) 
                 )
    
    PolyChain.isChainValid()
    print(PolyChain.chain)
