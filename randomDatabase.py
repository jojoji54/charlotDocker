import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

cred = credentials.Certificate(
    "charlotapp-firebase-adminsdk-y8n29-630f0f23a9.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# read data
# Getting a Document with a known ID

#Para hacer mas inteligente nuestra IA tenemos que guardar dos tipos de parametros , los que van a ser usador para pregunta y los que no van a ser u
#usados para nada , sin embargo servira para agrandar la base de datos de la IA, este archivo recupera los datos que no serviran
#para preguntas


intents = {"intents": []}#etiqueta del archivo json
detect_duplicate_by_tag = [] #variable que se usara para no duplicar entras

#Esto de abajo es una condicion la cual me permitira , no guardar archivos duplicados
with open('intents.json') as json_file:
    olddata = json.load(json_file)
    for ob in olddata['intents']:
        if not (ob["tag"] in detect_duplicate_by_tag):
            intents['intents'].append(ob)
            detect_duplicate_by_tag.append(ob["tag"])

#Esto de qui abajo, me permita recuperar los datos de la base de datos que tienen la etiqueta de la condicion
print("old data:", len(intents['intents']))
results = db.collection('users').document(
    'Peo5kqpi4GORXehD3oQVRXpHGfD2').collection('chatsRandom').get()
for index, result in enumerate(results):
    data = result.to_dict()
    if not (f"firebaseRandomdata{index}" in detect_duplicate_by_tag):
        intents["intents"].append({
            "tag": f"firebaseRandomdata{index}",
            "patterns":   [data["message"]],
            "responses":  [data["IAmessageAnswer1"],data["IAmessageAnswer2"],data["IAmessageAnswer3"],data["IAmessageAnswer4"],data["IAmessageAnswer5"],data["IAmessageAnswer6"]],
        })
        detect_duplicate_by_tag.append(f"firebaseRandomdata{index}")

#Una vez obtenidos los datos, y cmprobados los datos a no duplicar, lo guardamos en el archivo json
print("new data: ", len(intents['intents']))
with open("intents.json", "w") as outfile:
    json.dump(intents, outfile)
