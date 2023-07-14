from flask import Flask, jsonify, request #import objects from the flask model
app = Flask(__name__)

languages = [{'name' : 'JavaScript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]
@app.route('/', methods=['GET'])
def teset():
    return jsonify({'message':'It works!'})

#get all all languages
@app.route('/lang', methods=['GET'])
def reurnAll():
    return jsonify({'languages' : languages})

#get a specific language
@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language' : langs[0]})

#add language to list of languages
@app.route('/lang', methods=['GET', 'POST'])
def addOne():
    language = {'name' : request.json['name']} #get language
    languages.append(language) #add language to list of languages
    
    return jsonify({'languages' : languages})

#edit a language
@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify({'language' : langs[0]})

#delete a language 
@app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
    lang = [language for language in languages if language['name'] == name]
    languages.remove(lang[0])
    
    return jsonify({'languages' : languages})
            
if __name__ == '__main__':
    app.run(debug=True, port=8080) #run app on port 8080 in debug mode
