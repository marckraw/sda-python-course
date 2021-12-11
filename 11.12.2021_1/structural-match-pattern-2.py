# names = ['Krystian', 'Grzegorz', 'Paweł']
#
# match names:
#     case ['Krystian', 'Grzegorz', 'Paweł']:
#         print("Oto wlasciwa lista osob")
#     case _:
#         print("nieoczekiwana lista")

######################################################

# names = ['Krystian', 'Grzegorz', 'Paweł', 'Someone', 'Whatever']
#
# match names:
#     case _ if 'Krystian' in names:
#         print("Krystain jest w liscie")
#     case _:
#         print("nieoczekiwana lista")


######################################################

# names = ['Krystian', 'Grzegorz', 'Paweł', 'Someone', 'Whatever']
#
# match names:
#     case [_, 'Grzegorz', *rest]:
#         print("Oto wlasciwa lista osob")
#     case _:
#         print("nieoczekiwana lista")

######################################################

names = ['Krystian', 'Grzegorz', 'Paweł']

match names:
    case ['Krystian', _] | ['Krystian', _, _]:
        print("Oto wlasciwa lista osob")
    case _:
        print("nieoczekiwana lista")
