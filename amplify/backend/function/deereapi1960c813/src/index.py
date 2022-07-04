# Para layers tengo que tener importadas request y...bueno toda librería que necesite

import requests
import json
from requests.structures import CaseInsensitiveDict


boundary2 = {"id": "", "name": "", "area": "", "workableArea": "", "sourceType": "", "multipolygons": "",
             "@type": "", "extent": "", "active": "", "archived": "", "modifiedTime": "", "createdTime": "", "irrigated": ""}

boundaryDict = {}


def handler(event, context):

    header = CaseInsensitiveDict()
    organizationID = event['arguments']['organizationId']
    fieldId = event['arguments']['fieldId']
    # print("arguments :")
    # print(organizationID)
    header = {
        'User-Agent': 'Thunder Client (https://www.thunderclient.com)',
        'Accept': 'application/vnd.deere.axiom.v3+json',
        'Content-Type': 'application/json',
        "Authorization": "Bearer eyJraWQiOiJFRm5BQWw5SE5xQm02LXQ1ZHJWWFB3dzg3ZWEzSndhRkUyQTVaM2xpNjIwIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULmttbFFwTDU4U0pBeVRnYjZvc192WEdZQ3lNakNVazdYWWZiRnFXb0dhMTAub2Fyam16OGVuVFN4ZU5oUlg1ZDYiLCJpc3MiOiJodHRwczovL3NpZ25pbi5qb2huZGVlcmUuY29tL29hdXRoMi9hdXM3OHRubGF5c01yYUZoQzF0NyIsImF1ZCI6ImNvbS5kZWVyZS5pc2cuYXhpb20iLCJpYXQiOjE2NTY2ODQyNDcsImV4cCI6MTY1NjcyNzQ0NywiY2lkIjoiMG9hNWF4MjMwd29aM0MydU41ZDciLCJ1aWQiOiIwMHU1YXJmcDl2OFNPV3FSMTVkNyIsInNjcCI6WyJhZzIiLCJhZzEiLCJmaWxlcyIsIm9mZmxpbmVfYWNjZXNzIiwiYWczIiwib3JnMSIsIm9yZzIiLCJlcTIiLCJlcTEiXSwiYXV0aF90aW1lIjoxNjU2NjEwNzE5LCJzdWIiOiJqdWxpYW5tYXJzYWwifQ.HZARj1QujwN7YMlVTLFULxXzdx3QMeezy5YfTR0UEOfa4UJEW2R3sxjiHqzagggC19-pmfKu251V5waV6ksREJOYGQJO9evxgBZ9_Zyir9oD_mHiGs2I3xY8D40w9PY5subzH-Y0cAWgcfiUZoAUaVoET_8rsRpzEzsoX3B_gv3TWnq5ayDUtO1QI7crIb_Z6CqG2ou_ILrsUWIuyNUwC6YZkIh4s1TiMYhevEoFYnVZXWksiZVoHYaI9_f9uEjCyLK8todImCVA_WXZsowcjXJq2LvrO-j2J58gTvNKR9qMEe6LUsxQqNzMVkeHEdGaTxxwtr5dUmQzDaJWx98EOA"
    }
    response = requests.get(
        "https://sandboxapi.deere.com/platform/organizations/"+organizationID+"/fields/"+fieldId+"/boundaries", headers=header, auth={}).json()

    print("For response: ")
    for i in boundary2:
        if response["values"][0][i] is not None:
            boundary2[i] = response["values"][0][i]
    print("Boundary2: ")
    print(boundary2)
    print("\n")

    boundary2.update({
        "multipolygons": response["values"][0]["multipolygons"][0]["rings"][0]["points"]})
    print("a ver")
    print(response["values"][0]["multipolygons"][0]["rings"][0]["points"])
    print("\n")
    # print("Boundaries :")
    # print(response['values'][0]["multipolygons"]
    #      [0]['rings'])  # [0]['points'])

    # boundaries = response['values'][0]["multipolygons"][0]['rings']
    # [0]['points'])

# Al hacer una query de graphql en los argumentos viene por ej: 'arguments': {'organizationId': '123'}, con lo cual luego puedo usarla para invocar el callback con el code supongo
    print("constatación boundary2: ")
    print(boundary2)
    print("\n")

    # ver que hacer con el @ de @type
    boundaryDict.update({"type": response["values"][0]["@type"]})

    boundaryDict.update({"name": response["values"][0]["name"]})

    boundaryDict.update({"sourceType": response["values"][0]["sourceType"]})

    boundaryDict.update({"createdTime": response["values"][0]["createdTime"]})

    boundaryDict.update(
        {"modifiedTime": response["values"][0]["modifiedTime"]})

    boundaryDict.update({"area": response["values"][0]["area"]})
    boundaryDict["area"].update({"type": boundaryDict["area"]["@type"]})

    boundaryDict.update(
        {"workableArea": response["values"][0]["workableArea"]})

    boundaryDict["workableArea"].update(
        {"type": boundaryDict["workableArea"]["@type"]})
    multipolygons1 = boundaryDict.update(
        {"multipolygons": response["values"][0]["multipolygons"]})
    # Acá luego se haría con un for porque pueden haber varios boundarys, por ahora hago [0]
    # rings dentro de el la lista de Rings tiene una propiedad type:"exterior", reever eso.
    boundaryDict["multipolygons"][0].update(
        {"type": boundaryDict["multipolygons"][0]["@type"]})
    # con esto hago el for de multipolygons tal vez
    # for cliente in response["values"]:
    #   clientDict[cliente["name"]] = cliente["name"]

    boundaryDict.update({"extent": response["values"][0]["extent"]})
    boundaryDict["extent"].update({"type": boundaryDict["extent"]["@type"]})
    boundaryDict["extent"]["topLeft"].update(
        {"type": boundaryDict["extent"]["topLeft"]["@type"]})
    boundaryDict["extent"]["bottomRight"].update(
        {"type": boundaryDict["extent"]["bottomRight"]["@type"]})

    boundaryDict.update({"archived": response["values"][0]["archived"]})

    boundaryDict.update({"id": response["values"][0]["id"]})

    boundaryDict.update({"active": response["values"][0]["active"]})

    boundaryDict.update({"irrigated": response["values"][0]["irrigated"]})

    print("Print del campo actual :")
    print(boundaryDict)
    print("\n")

    return boundaryDict
# json.dumps('Hello from your new Amplify Python lambda!')
# 'body':  boundary2
