#! /usr/bin/env python
import csv
import os
import glob
import shutil
with open('/RepSeq/RS_Processed/iReceptor/DataToload/comparison/filelist.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    te=["/RepSeq/RS_Processed/iReceptor/DataToLoad/comparison/ireceptorFiletmp/"+row[0] for row in csv_reader if row]
    print(te)
filel = glob.glob("/RepSeq/RS_Processed/iReceptor/DataToLoad/comparison/ireceptorFiletmp/*ireceptor.txt")
cnt=0
for fileiR in filel:
    if fileiR not in te:
        shutil.move(fileiR,"/RepSeq/RS_Processed/iReceptor/DataToLoad/comparison/ireceptorFile")
        print(fileiR)
        cnt+=1

print(cnt)