persoon = {"naam": "Ali", "leeftijd": 30}
try:
    print(persoon["adres"])
except KeyError as ex :
    print(f"{ex} bestaat nie geef juiste naam in")