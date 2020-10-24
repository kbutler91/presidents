import requests
import json

url_ddg = "https://api.duckduckgo.com"
url = "https://api.duckduckgo.com/?q=presidents of the united states&format=json"

def test_Lincoln():
    resp = requests.get(url)
    rsp_data = resp.json()
    json_string = json.dumps(rsp_data, indent=4, sort_keys=True)
    print(json_string)
    assert "Lincoln" in rsp_data["RelatedTopics"][0]["Text"]

def test_Jackson():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Jackson" in rsp_data["RelatedTopics"][1]["Text"]

def test_Johnson():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Johnson" in rsp_data["RelatedTopics"][2]["Text"]

def test_Obama():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Obama" in rsp_data["RelatedTopics"][3]["Text"]

def test_Harrison():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Harrison" in rsp_data["RelatedTopics"][4]["Text"]

def test_Buren():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Buren" in rsp_data["RelatedTopics"][5]["Text"]

def test_Clinton():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Clinton" in rsp_data["RelatedTopics"][6]["Text"]

def test_Coolidge():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Coolidge" in rsp_data["RelatedTopics"][7]["Text"]

def test_Arthur():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Arthur" in rsp_data["RelatedTopics"][8]["Text"]

def test_Trump():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Trump" in rsp_data["RelatedTopics"][9]["Text"]

def test_Eisenhower():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Eisenhower" in rsp_data["RelatedTopics"][10]["Text"]

def test_Roosevelt():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Roosevelt" in rsp_data["RelatedTopics"][11]["Text"]

def test_Pierce():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Pierce" in rsp_data["RelatedTopics"][12]["Text"]

def test_Bush():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Bush" in rsp_data["RelatedTopics"][14]["Text"]

def test_Washington():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Washington" in rsp_data["RelatedTopics"][15]["Text"]

def test_BushW():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Bush" in rsp_data["RelatedTopics"][16]["Text"]

def test_Ford():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Ford" in rsp_data["RelatedTopics"][17]["Text"]

def test_Cleveland():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Cleveland" in rsp_data["RelatedTopics"][18]["Text"]

def test_Truman():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Truman" in rsp_data["RelatedTopics"][19]["Text"]

def test_Hoover():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Hoover" in rsp_data["RelatedTopics"][20]["Text"]

def test_Garfield():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Garfield" in rsp_data["RelatedTopics"][22]["Text"]

def test_Buchanan():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Buchanan" in rsp_data["RelatedTopics"][23]["Text"]

def test_Polk():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Polk" in rsp_data["RelatedTopics"][24]["Text"]

def test_Madison():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Madison" in rsp_data["RelatedTopics"][25]["Text"]

def test_Monroe():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Monroe" in rsp_data["RelatedTopics"][26]["Text"]

def test_Carter():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Carter" in rsp_data["RelatedTopics"][27]["Text"]

def test_Adams():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Adams" in rsp_data["RelatedTopics"][28]["Text"]

def test_Kennedy():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Kennedy" in rsp_data["RelatedTopics"][29]["Text"]

def test_AdamsQ():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Quincy Adams" in rsp_data["RelatedTopics"][30]["Text"]

def test_Tyler():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Tyler" in rsp_data["RelatedTopics"][31]["Text"]

def test_JohnsonB():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "B. Johnson" in rsp_data["RelatedTopics"][34]["Text"]

def test_Fillmore():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Fillmore" in rsp_data["RelatedTopics"][37]["Text"]

def test_Nixon():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Nixon" in rsp_data["RelatedTopics"][39]["Text"]

def test_Reagan():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Reagan" in rsp_data["RelatedTopics"][40]["Text"]

def test_Hayes():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Hayes" in rsp_data["RelatedTopics"][41]["Text"]

def test_Jefferson():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Jefferson" in rsp_data["RelatedTopics"][44]["Text"]

def test_Grant():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Grant" in rsp_data["RelatedTopics"][45]["Text"]

def test_Harding():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Harding" in rsp_data["RelatedTopics"][46]["Text"]

def test_Taft():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Taft" in rsp_data["RelatedTopics"][48]["Text"]

def test_McKinley():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "McKinley" in rsp_data["RelatedTopics"][49]["Text"]

def test_Wilson():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Wilson" in rsp_data["RelatedTopics"][50]["Text"]

def test_Taylor():
    resp = requests.get(url)
    rsp_data = resp.json()
    assert "Taylor" in rsp_data["RelatedTopics"][51]["Text"]
