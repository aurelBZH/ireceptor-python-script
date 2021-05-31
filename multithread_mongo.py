from multiprocessing.dummy import Pool as ThreadPool 

from pymongo import MongoClient


def my_function(repertoire_id):
    return db.sequence.count({"repertoire_id":repertoire_id})

def delete_many_rep(repertoire_id):
    return db.sequence.delete_many({"repertoire_id":repertoire_id})

def list_sample(study_id):
    list_samples=[]
    for sample in db.sample.find({'study_id': study_id}):
        list_samples.append(sample["repertoire_id"])
    return list_samples



if __name__=="main":
    client = MongoClient('ireceptor-database', 27017)
    db = client['ireceptor']

    thread_pool_size = 4
    pool = ThreadPool(thread_pool_size) 
    test_list = list_sample("PRJNA486323")
    result_list = pool.map(my_function, test_list)
    print(result_list)