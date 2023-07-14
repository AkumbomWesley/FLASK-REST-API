from flask import Flask, jsonify, request #import objects from the flask model
app = Flask(__name__)

@app.route('/', methods=['GET'])
def teset():
    return jsonify({'message':'It works!'})

#if __name__ == '__main__':
    
