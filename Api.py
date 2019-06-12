# the main api - having different api endpoints

from flask import Flask,request,jsonify
from Processors import Processor

# initializing the Flask app
app = Flask(__name__)
# initializing the processor class object
processor = Processor();

        
@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/openingHours' , methods = ['POST'])
def api_articles():
    if request.args['data'] != '' or request.args['data'] != {}:
        rough_data = request.args['data']
        result = processor.run(rough_data)
        return jsonify(result)
    else:
        return jsonify([])

if __name__ == '__main__':
    app.run()