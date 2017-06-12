#!/usr/bin/python
# Filename: ImageUrl_Process.py
# -*- coding:utf-8 -*-

import pymongo


def update_item(line, db):
    line = line.split('|')
    artical = db.artical.find_one({"title_hash":line[0]})
    if(not artical):
        print(line[0] + " not exists")
        return
    db['artical'].update({'title':line[0]}, {'$set':{'image_url':line[1], 'source_url':line[2]}})
    line[3] = line[3].replace('\n','')
    db['artical_tag'].update({'a_id':str(artical['_id'])}, {'$set':{'catagore':line[3]}})

#db.Account.update({"UserName":"libing"},{"$set":{"Email":"libing@126.com","Password":"123"}})

client = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = client['ArticalRecommend']

with open("tmp_imageurl", 'rb') as f:
    for line in f:
        line = str(line, "utf-8")
        update_item(line, db)