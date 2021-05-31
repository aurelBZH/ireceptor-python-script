import pymongo
import json 
import pandas
import math
import pprint


samplesheet= pandas.read_csv("/home/mhanna_metadata.csv")
samplesheet=samplesheet.set_index("repertoire_id")
# with open("/mnt/mukkuri/RepSeq/RS_Analysis/ABEL/vmh_samplesf.json","r") as jsonfileread:
#     samplesjson = json.load(jsonfileread)
db = pymongo.MongoClient("ireceptor-database").ireceptor

for sampledb in db.sample.find({"submitted_by":"Vanessa Mhanna"}):
    sample = samplesheet.loc[sampledb["repertoire_id"]]
    for val in sample.iteritems():
        if val[0] in sampledb:
            if  sampledb[val[0]]!=val[1] and pandas.isna(val[1])== False :
                    #db.sample.find_one_and_update({"repertoire_id":sample["repertoire_id"]}, { '$set': { val[0] : val[1]} }, 
                    #    return_document = pymongo.collection.ReturnDocument.AFTER)))
                    findedsam = db.sample.find_one({"repertoire_id":sampledb["repertoire_id"]})
                    pprint.pprint(findedsam)