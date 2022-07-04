import requests


def handler(event, context):
    organizationID = event['arguments']['organizationId']
    header = {
        'User-Agent': 'Thunder Client (https://www.thunderclient.com)',
        'Accept': 'application/vnd.deere.axiom.v3+json',
        'Content-Type': 'application/json',
        "Authorization": "Bearer eyJraWQiOiJFRm5BQWw5SE5xQm02LXQ1ZHJWWFB3dzg3ZWEzSndhRkUyQTVaM2xpNjIwIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULmttbFFwTDU4U0pBeVRnYjZvc192WEdZQ3lNakNVazdYWWZiRnFXb0dhMTAub2Fyam16OGVuVFN4ZU5oUlg1ZDYiLCJpc3MiOiJodHRwczovL3NpZ25pbi5qb2huZGVlcmUuY29tL29hdXRoMi9hdXM3OHRubGF5c01yYUZoQzF0NyIsImF1ZCI6ImNvbS5kZWVyZS5pc2cuYXhpb20iLCJpYXQiOjE2NTY2ODQyNDcsImV4cCI6MTY1NjcyNzQ0NywiY2lkIjoiMG9hNWF4MjMwd29aM0MydU41ZDciLCJ1aWQiOiIwMHU1YXJmcDl2OFNPV3FSMTVkNyIsInNjcCI6WyJhZzIiLCJhZzEiLCJmaWxlcyIsIm9mZmxpbmVfYWNjZXNzIiwiYWczIiwib3JnMSIsIm9yZzIiLCJlcTIiLCJlcTEiXSwiYXV0aF90aW1lIjoxNjU2NjEwNzE5LCJzdWIiOiJqdWxpYW5tYXJzYWwifQ.HZARj1QujwN7YMlVTLFULxXzdx3QMeezy5YfTR0UEOfa4UJEW2R3sxjiHqzagggC19-pmfKu251V5waV6ksREJOYGQJO9evxgBZ9_Zyir9oD_mHiGs2I3xY8D40w9PY5subzH-Y0cAWgcfiUZoAUaVoET_8rsRpzEzsoX3B_gv3TWnq5ayDUtO1QI7crIb_Z6CqG2ou_ILrsUWIuyNUwC6YZkIh4s1TiMYhevEoFYnVZXWksiZVoHYaI9_f9uEjCyLK8todImCVA_WXZsowcjXJq2LvrO-j2J58gTvNKR9qMEe6LUsxQqNzMVkeHEdGaTxxwtr5dUmQzDaJWx98EOA"
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
