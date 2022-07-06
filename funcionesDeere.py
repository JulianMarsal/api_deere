import requests


def handler(event, context):
    organizationID = event['arguments']['organizationId']
    header = {
        'User-Agent': 'Thunder Client (https://www.thunderclient.com)',
        'Accept': 'application/vnd.deere.axiom.v3+json',
        'Content-Type': 'application/json',
        "Authorization": "Bearer eyJraWQiOiJFRm5BQWw5SE5xQm02LXQ1ZHJWWFB3dzg3ZWEzSndhRkUyQTVaM2xpNjIwIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULm1mMU5xOGNYbUZsbldOTFBPTEVwbGJPcXlYc1lYVjhmbjV5cGRJbkNwSDQub2FyanYyMnIyNDhvRzQ0cHc1ZDYiLCJpc3MiOiJodHRwczovL3NpZ25pbi5qb2huZGVlcmUuY29tL29hdXRoMi9hdXM3OHRubGF5c01yYUZoQzF0NyIsImF1ZCI6ImNvbS5kZWVyZS5pc2cuYXhpb20iLCJpYXQiOjE2NTcxMTk3MzQsImV4cCI6MTY1NzE2MjkzNCwiY2lkIjoiMG9hNWF4MjMwd29aM0MydU41ZDciLCJ1aWQiOiIwMHU1YXJmcDl2OFNPV3FSMTVkNyIsInNjcCI6WyJhZzIiLCJhZzEiLCJmaWxlcyIsIm9mZmxpbmVfYWNjZXNzIiwiYWczIiwib3JnMSIsIm9yZzIiLCJlcTIiLCJlcTEiXSwiYXV0aF90aW1lIjoxNjU2OTQxNDc0LCJzdWIiOiJqdWxpYW5tYXJzYWwifQ.IdiUyjVDJtdiA9EuBCUVmKgUzUDUIH0E2_hwmisP1UiYeDGiTnCZFA1DsNL2BGlbEb81lsxComUw4J-t_ihHCeRnIZMlM7tit_P4sktBV7b74Zm_KWZZJCy5uPlRv-7l8giKQl-GSGoEwI1_INrnTcykRkS-byYn783xp8_Xx43oltcPUd-lQ3o-CLbfpi9JQzlrd0jfnnfLNwVLR_jcuU6c8lrTLC5ir13GgD3lgTRshQ49Qlu0frzsIeArwjMg-uG-tfMbJprpuAgTh6pPOovO9HgmOwZOwfIDW785-CTXanGO_I_TauG2VO7ZUj_3z2g5G9mbQywH2Dr2B9pL3Q"
    }
    response = requests.get("https://sandboxapi.deere.com/platform/organizations/" +
                            organizationID+"/clients", headers=header).json()

    clientList = []
    for cliente in response["values"]:
        clientDict = {}
        clientDict.update({"name": cliente["name"]})
        clientDict.update({"archived": cliente["archived"]})
        clientDict.update({"id": cliente["id"]})
        clientLinks = []
        for link in cliente["links"]:
            clientLinks.append(link)
        clientDict.update({"links": clientLinks})
        clientList.append(clientDict)
    return clientList


# ----------------------------------------------------------------------------------------------------------------------


def handler(event, context):
    organizationID = event['arguments']['organizationId']
    header = {
        'User-Agent': 'Thunder Client (https://www.thunderclient.com)',
        'Accept': 'application/vnd.deere.axiom.v3+json',
        'Content-Type': 'application/json',
        "Authorization": "Bearer eyJraWQiOiJFRm5BQWw5SE5xQm02LXQ1ZHJWWFB3dzg3ZWEzSndhRkUyQTVaM2xpNjIwIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULm1mMU5xOGNYbUZsbldOTFBPTEVwbGJPcXlYc1lYVjhmbjV5cGRJbkNwSDQub2FyanYyMnIyNDhvRzQ0cHc1ZDYiLCJpc3MiOiJodHRwczovL3NpZ25pbi5qb2huZGVlcmUuY29tL29hdXRoMi9hdXM3OHRubGF5c01yYUZoQzF0NyIsImF1ZCI6ImNvbS5kZWVyZS5pc2cuYXhpb20iLCJpYXQiOjE2NTcxMTk3MzQsImV4cCI6MTY1NzE2MjkzNCwiY2lkIjoiMG9hNWF4MjMwd29aM0MydU41ZDciLCJ1aWQiOiIwMHU1YXJmcDl2OFNPV3FSMTVkNyIsInNjcCI6WyJhZzIiLCJhZzEiLCJmaWxlcyIsIm9mZmxpbmVfYWNjZXNzIiwiYWczIiwib3JnMSIsIm9yZzIiLCJlcTIiLCJlcTEiXSwiYXV0aF90aW1lIjoxNjU2OTQxNDc0LCJzdWIiOiJqdWxpYW5tYXJzYWwifQ.IdiUyjVDJtdiA9EuBCUVmKgUzUDUIH0E2_hwmisP1UiYeDGiTnCZFA1DsNL2BGlbEb81lsxComUw4J-t_ihHCeRnIZMlM7tit_P4sktBV7b74Zm_KWZZJCy5uPlRv-7l8giKQl-GSGoEwI1_INrnTcykRkS-byYn783xp8_Xx43oltcPUd-lQ3o-CLbfpi9JQzlrd0jfnnfLNwVLR_jcuU6c8lrTLC5ir13GgD3lgTRshQ49Qlu0frzsIeArwjMg-uG-tfMbJprpuAgTh6pPOovO9HgmOwZOwfIDW785-CTXanGO_I_TauG2VO7ZUj_3z2g5G9mbQywH2Dr2B9pL3Q"
    }
    response = requests.get("https://sandboxapi.deere.com/platform/organizations/" +
                            organizationID+"/fields", headers=header).json()

    fieldList = []
    for field in response["values"]:
        fieldDict = {}
        fieldDict["type"] = field["@type"]  # ver que onda esta nomenglatura
        fieldDict["name"] = field["name"]
        fieldDict["archived"] = field["archived"]
        fieldDict["id"] = field["id"]
        fieldLinks = []
        for link in field["links"]:
            fieldLinks.append(link)
        fieldDict["links"] = fieldLinks
        fieldList.append(fieldDict)
    return fieldList


# ----------------------------------------------------------------------------------------------------------------------


def handler(event, context):

    # Para el entorno de prueba
    # if(process.env.Authorization is not None):
    #    console.log(process.env.Authorization)
    organizationID = event['arguments']['organizationId']
    fieldId = event['arguments']['fieldId']
    # headers["Authorization"] = "Bearer {token}" así se podría hacer para no pasar el "bearer" también
    header = {
        'User-Agent': 'Thunder Client (https://www.thunderclient.com)',
        'Accept': 'application/vnd.deere.axiom.v3+json',
        'Content-Type': 'application/json',
        "Authorization": "Bearer eyJraWQiOiJFRm5BQWw5SE5xQm02LXQ1ZHJWWFB3dzg3ZWEzSndhRkUyQTVaM2xpNjIwIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULm1mMU5xOGNYbUZsbldOTFBPTEVwbGJPcXlYc1lYVjhmbjV5cGRJbkNwSDQub2FyanYyMnIyNDhvRzQ0cHc1ZDYiLCJpc3MiOiJodHRwczovL3NpZ25pbi5qb2huZGVlcmUuY29tL29hdXRoMi9hdXM3OHRubGF5c01yYUZoQzF0NyIsImF1ZCI6ImNvbS5kZWVyZS5pc2cuYXhpb20iLCJpYXQiOjE2NTcxMTk3MzQsImV4cCI6MTY1NzE2MjkzNCwiY2lkIjoiMG9hNWF4MjMwd29aM0MydU41ZDciLCJ1aWQiOiIwMHU1YXJmcDl2OFNPV3FSMTVkNyIsInNjcCI6WyJhZzIiLCJhZzEiLCJmaWxlcyIsIm9mZmxpbmVfYWNjZXNzIiwiYWczIiwib3JnMSIsIm9yZzIiLCJlcTIiLCJlcTEiXSwiYXV0aF90aW1lIjoxNjU2OTQxNDc0LCJzdWIiOiJqdWxpYW5tYXJzYWwifQ.IdiUyjVDJtdiA9EuBCUVmKgUzUDUIH0E2_hwmisP1UiYeDGiTnCZFA1DsNL2BGlbEb81lsxComUw4J-t_ihHCeRnIZMlM7tit_P4sktBV7b74Zm_KWZZJCy5uPlRv-7l8giKQl-GSGoEwI1_INrnTcykRkS-byYn783xp8_Xx43oltcPUd-lQ3o-CLbfpi9JQzlrd0jfnnfLNwVLR_jcuU6c8lrTLC5ir13GgD3lgTRshQ49Qlu0frzsIeArwjMg-uG-tfMbJprpuAgTh6pPOovO9HgmOwZOwfIDW785-CTXanGO_I_TauG2VO7ZUj_3z2g5G9mbQywH2Dr2B9pL3Q"
    }
    response = requests.get(
        "https://sandboxapi.deere.com/platform/organizations/"+organizationID+"/fields/"+fieldId+"/boundaries", headers=header, auth={}).json()
    # For each field in response, create a dictionary and add it to the list
    # print("For response: ")
    # for i in boundary:
    #     if response["values"][0][i] is not None:
    #         boundary[i] = response["values"][0][i]

    # boundary.update({
    #     "multipolygons": response["values"][0]["multipolygons"][0]["rings"][0]["points"]})

    boundaryDict = {"id": "", "name": "", "area": "", "workableArea": "", "sourceType": "", "multipolygons": [],
                    "type": "", "extent": "", "active": None, "archived": None, "modifiedTime": "", "createdTime": "", "irrigated": None}

    if (response["total"] == 0):
        # "No boundaries found"
        print("No boundaries found")
        return boundaryDict

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
    boundaryDict.update(
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

    return boundaryDict
