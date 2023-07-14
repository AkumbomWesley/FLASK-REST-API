from flask import Flask, jsonify, request #import objects from the flask model
app = Flask(__name__)

@app.route('/', methods=['GET'])
def teset():
    return jsonify({'message':'It works!'})

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app on port 8080 in debug mode
