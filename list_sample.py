
import pymongo
import json 
import pandas
import math
import pprint

# connection a la db mongo
db=pymongo.MongoClient("ireceptor-database").ireceptor


def list_samples(study_id):
    dict_samples={}
    with open(f"{study_id}.json", "w") as sample_list_file:
        for sample in db.sample.find({'study_id': study_id}):
            dict_samples[sample["repertoire_id"]]=sample['data_processing_files']
        json.dump(dict_samples,sample_list_file)
    return dict_samples

if __name__=="main":

    list_samples("PRJNA486323")