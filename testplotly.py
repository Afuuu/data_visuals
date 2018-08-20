# -*- coding:utf-8 -*-
import pymongo



import plotly.offline as of
import plotly.graph_objs as go


class MongodbConn(object):
    serial_numbers = []
    movie_names = []
    stars = []
    evaluates = []
    def __init__(self):
        self.CONN = pymongo.MongoClient("127.0.0.1", 27017)


    def run(self):
        database = "douban"
        db = self.CONN[database]
        #db.authenticate("username", "password")
        col = db.collection_names()
        #col为datbases list
        print(col)
        #第一个数据库（第0个表中250部电影，第1个表中25部电影）
        col = col[1]
        collection = db.get_collection(col)
        # query one document
        document = collection.find_one()['movie_name']
        print(document)

        # query all document
        #documents = collection.find({},{'serial_number':1,'_id':0})
        documents = collection.find()
        for i in documents:
            # print key of (key: value)
            #print(i.keys())
            #print(i.values())
            #print(i['serial_number'])
            self.serial_numbers.append(i['serial_number'])
            #print(i['movie_name'])
            self.movie_names.append(i['movie_name'])
            self.stars.append(i['star'])
            #print(i['evaluate'].strip('人评价'))
            self.evaluates.append(int(i['evaluate'].strip('人评价'))/10000) #原始数据度简单处理
            if i['describe'] != "":
                with open('/Users/fuchuang/wordcloudtest/douban_movie.txt', 'a') as f:
                    f.write(i['describe'])


if __name__ == '__main__':
    mongo_obj = MongodbConn()
    mongo_obj.run()

    of.offline.init_notebook_mode(connected=True)
    trace0 = go.Scatter(
        y=mongo_obj.movie_names,
        x=mongo_obj.serial_numbers,
        mode='markers',
        marker=dict(size=mongo_obj.evaluates,),
        name='关注度'
    )

    trace1 = go.Scatter(
        x=mongo_obj.serial_numbers,
        y=mongo_obj.stars,
        name='评分'
    )
    #data = go.Data([trace0, trace1])
    data = go.Data([trace0])  #关注度bubble图
    #data = go.Data([trace1]) #评分折线图


    of.plot(data)




