import csv

d={}
with open("data.csv", 'r') as data_file:
    data = csv.DictReader(data_file, delimiter=",")
    for row in data:

        item = d.get(row["ZIPCODE"], dict())

        item[row["RESTNAME"]] = int(row["DISCOUNT"])

        d[row["ZIPCODE"]] = item

userzip = input("Please enter your zip-code: ")

if userzip in d.keys():
    a = d.get(userzip)
    b = a.values()
    c = list(b)
    e = max(c)
    print("!TODAY'S DISCOUNTS!", "Zip:"+" "+userzip)
    for resto in a:
        print(resto, ":", str(a.get(resto))+"%","OFF")
    print("Enjoy your meal!")
else:
    print("Sorry, no available restaurants in your area!")



