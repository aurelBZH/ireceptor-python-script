import pymongo
import json 
import pandas
import math
import pprint

# metadata file cpoied in the vm home
samplesheet= pandas.read_csv("/home/mhanna_metadata.csv")
# need repertoire id as row index
samplesheet=samplesheet.set_index("repertoire_id")
# with open("/mnt/mukkuri/RepSeq/RS_Analysis/ABEL/vmh_samplesf.json","r") as jsonfileread:
#     samplesjson = json.load(jsonfileread)
# connection to the database
db = pymongo.MongoClient("ireceptor-database").ireceptor

# work on sample from the  V mhanna study
# loop on the samples metadata in the database
for sampledb in db.sample.find({"submitted_by":"Vanessa Mhanna"}):
    # get the sample that as the same repertoire_id in the metadata file  
    sample = samplesheet.loc[sampledb["repertoire_id"]]
    # loop on the items of the dataframe
    for val in sample.iteritems():
        # the item exist in the database and if the value in the metadata sheet is different 
        # from the one in the database and is not NA replace the value in the database
        # by the value of the dataframe
        # take car to not modify the repertoire_id which may cause probleme in the database
        # ( breaking connection between sample and sequence)
        if val[0] in sampledb:
            if  sampledb[val[0]]!=val[1] and pandas.isna(val[1])== False :
                    # replace value in the database by the value in the dataframe
                    db.sample.find_one_and_update({"repertoire_id":sample["repertoire_id"]}, { '$set': { val[0] : val[1]} }, 
                        return_document = pymongo.collection.ReturnDocument.AFTER)))
                    #findedsam = db.sample.find_one({"repertoire_id":sampledb["repertoire_id"]})
                    pprint.pprint(findedsam)