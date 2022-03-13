from flask import Flask, jsonify, request
dinosarusDB=[
{
"lifespan" : "28",
"name": "terex",
"geolocation" : "north america",
"foodtype": "carnivours"
},
{
"lifespan" : "20",
"name": "velociraptor",
"geolocation" : "eastern asia",
"foodtype": "carnivours"
}
]
app = Flask(__name__)

@app.route("/", methods=['GET'])
def test():
    return jsonify({'message': "it work!"})

@app.route('/dinosarus/getDinosarus', methods=['GET'])
def getDinosarus():
    return jsonify({'dino': dinosarusDB})


@app.route('/dinosarus/getDinosaru/<lifespan>', methods=['GET'])
def getDinosaruDetail(lifespan):
    dinosarus = [dinos for dinos in dinosarusDB if (dinos['lifespan']==lifespan)]
    print(dinosarus)
    return jsonify({'dinos' : dinosarus})

@app.route('/dinosarus/updateDinosaru/<lifespan>', methods=['PUT'])
def updateDinosaruDetail(lifespan):
    dinosarus = [dinos for dinos in dinosarusDB if (dinos['lifespan'] == lifespan)]

    if('lifespan' in request.json):
        print('Dinosaru Available')
    if ('name' in request.json):
        dinosarus[0]['name'] = request.json['name']
    return jsonify({'dinos': dinosarus[0]})

@app.route('/dinosarus/addDinosaru', methods=['POST'])
def addDinosaru() :
    dinosarus = {
        "lifespan" :request.json["lifespan"],
        "name":request.json["name"],
        "geolocation" :request.json["geolocation"],
        "foodtype":request.json["foodtype"]
    }
    dinosarusDB.append(dinosarus)
    return jsonify({'dino': dinosarusDB})

@app.route('/dinosarus/removeDinosaru/<lifespan>', methods=['DELETE'])
def removeDinosaru(lifespan):
    dinosarus = [dinos for dinos in dinosarusDB if (dinos['lifespan'] == lifespan)]
    if(len(dinosarus) > 0):
        dinosarusDB.remove(dinosarus[0])
    return jsonify({'dinos': dinosarus})

if __name__ == "__main__":
    app.run(debug=True)
