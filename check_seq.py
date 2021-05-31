import pymongo
import json 
import pandas
import math
import pprint
import sys

db = pymongo.MongoClient("ireceptor-database").ireceptor
print('Argument List:', str(sys.argv))

# a simple script to check if sample submitted by Vanessa Mhanna contains sequence

for sampleDb in db.sample.find({"submitted_by":sys.argv[0]}):
    countSeq = db.sequence.count({"repertoire_id":sampledb["repertoire_id"]})
    if countSeq == 0:
        print("alert this repertoire_has zero sequence")
    else:
        print(f"this repertoire has{countSeq} sequence.")
