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
                            organizationID+"/fields", headers=header).json()

    fieldList = []
    print("response con error")
    print(response)
    print("\n")
    if response["errors"]:
        raise Exception('Invalid Link!')
        raise ValueError("La edad debe ser positiva.")

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
