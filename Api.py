# the main api - having different api endpoints
# from flask import Flask, request
# from flask_restful import Resource, Api
# from sqlalchemy import create_engine
# from json import dumps



# app = Flask(__name__)
# api = Api(app)



# class ApiCall(Resource):
#     def post(self, employee_id):
#         status = Processor.checkOpenOrClose();
#         return [int(employee_id),status]
        
# api.add_resource(ApiCall, '/employees/<employee_id>') # Route_3


# if __name__ == '__main__':
#      app.run(port='5000')


from flask import Flask, url_for , request
from Processors import Processor

app = Flask(__name__)

process = Processor();

        
@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles' , methods = ['POST'])
def api_articles():
    if request.args['data'] != '':
        rough_data = request.args['data']
        process.run(rough_data)
        return "True"
    else:
        return "false"

if __name__ == '__main__':
    app.run()