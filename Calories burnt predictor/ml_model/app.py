from flask import Flask
from flask import request, jsonify
from ml_project import mod

from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)

def parse_request():
    data = request.get_json() # data is empty
    print(data)
    res = mod(float(data['gender']), float(data['age']), float(data['height']), float(data['weight']), float(data['duration']), float(data['heartrate']), float(data['bodytemp']))
    ans=jsonify({'result':res})
    return ans
    # content_type = request.headers.get('Content-Type')
    # if (content_type == 'application/json'):
    #     json = request.json
    #     print("received info: "+json)
    #     res=mod(json['gender'],json['age'],json['height'],json['weight'],json['duration'],json['heartrate'],json['bodytemp'])
    #     print("result: "+res)
    #     return res
    # else:
    #     return 'Content-Type not supported!'




if __name__ == "__main__":
	app.run()