



dziennik = {
    3: 'Maria',
    19: 'Ada',
    17: 'Bartek',
    27: 'Tomasz'
}

metryki = {
    "Daniel": 19,
    "Bartek": 30,
    "Ala": 33
}

print(dziennik)

if 30 in dziennik:
    print(dziennik[3])
else:
    print("nie ma takiego numeru")


print(metryki["Bartek"])

metryki["Bartek"] += 5

print(metryki["Bartek"])


print(metryki.items())
print(metryki.keys())


#######################################

imiona = ['Bartek', 'Ala', 'Ela', 'Something']
wzrosty = [1.8, 1.65, 1.78, 23]

print(list(zip(imiona, wzrosty)))

dict_wzrostow = { k:v for (k, v) in zip(imiona, wzrosty) }
print(dict_wzrostow)

