from flask import Flask,request
from flask_restful import Api, Resource,reqparse,abort
app = Flask(__name__)
api = Api(app)
data = {"Tanish":{"age":22,"gender":"male"}}
video_put_args = reqparse.RequestParser()
# class HelloWorld(Resource):
#     def get(self,name):
video_put_args.add_argument('name',type=str,help ='Please Enter Name of The video',required = True)
video_put_args.add_argument('views',type=int,help ='Please Enter Number of views on video',required = True)
video_put_args.add_argument('likes',type=bool,help ='Please Enter Number of likes on video',required = True)
#         return data[name] # this is a json format
#         # data we need to return json format only
# api.add_resource(HelloWorld,"/helloworld/<string:name>") 
video = {}
def Not_exist(video_id):
    if video_id not in video:
        abort(404,message="Video did not exist")
def Exist(video_id):
    if video_id in video:
        abort(409,message="The video exists already")
class Video(Resource):
    def get(self,video_id):
        Not_exist(video_id)
        return video[video_id]
    def post(self,video_id):
        Exist(video_id)
        args = video_put_args.parse_args()
        video[video_id]=args
        return video[video_id] ,201
    def delete(self,video_id):
        Not_exist(video_id)
        del video[video_id]
        return '',204
         
api.add_resource(Video,"/video/<int:video_id>")
# here we are accesing api class method add_resource , and this take class
# which is inheriented from resource class , after that were we want to show this 

if __name__ =="__main__":
    app.run(debug=True)