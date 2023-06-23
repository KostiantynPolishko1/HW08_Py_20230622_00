# Data
# contacts = {"Kostiantyn": "+38-073-340-90-97",
#             "Margarita": "+38-096-835-60-27",
#             "Dariya": "+38-066-645-98-81"
# }

while True:
    print("Contacts menu:")
    print("\t0 -> EXIT!"
          "\n\t1 -> show contacts"
          "\n\t2 -> add new contacts"
          "\n\t3 -> delete contacts"
          "\n\t4 -> modify contacts"
          "\n\t5 -> search contacts")
    n = input("enter num. operations -> ")
    try:
        n = abs(int(n))
        if n > 5:
            print("\n\tERROR!" + str(n) + "is out of range 0...6\n")
            continue
    except:
        print("\n\tERROR! Enter int. value\n")
        continue
    print("operation", n)

    if n == 0:
        print("\n\tEXIT!")
        break

# print("\n\tContacts:")
# for name in contacts:
#     print(name + ",\tmob: " + contacts[name])
#
# print("\nadd new contacts:")
# name = input("\tenter name\t-> ")
# mob_num = input("\tenter mob.num\t-> ")
#
# contacts[name] = mob_num
#
# print("\n\tContacts:")
# for name in contacts:
#     print(name + ",\tmob: " + contacts[name])

