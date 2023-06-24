
#Data
contacts = {"Kostiantyn": "+38-073-340-90-97",
            "Margarita": "+38-096-835-60-27",
            "Dariya": "+38-066-645-98-81"
}

while True:
    print("\nContacts menu:")
    print("\t0 -> EXIT!"
          "\n\t1 -> show contacts"
          "\n\t2 -> add new contacts"
          "\n\t3 -> delete contacts"
          "\n\t4 -> modify contacts"
          "\n\t5 -> search contacts")
    n = input("\t\tenter num. operations -> ")
    try:
        n = abs(int(n))
        if n > 5:
            print("\n\tERROR!\n\t" + str(n) + "is out of range 0...6\n")
            continue
    except:
        print("\n\tERROR! Enter int. value\n")
        continue
    print("\t\toperation", n)

    if n == 0:
        print("\n\tEXIT!")
        break

    elif n == 1:
        print("\n\tList of contacts", end='')
        if not len(contacts):
            print(" is empty", contacts)
        else:
            print(":")
            for name in contacts:
                print(name + ",\tmob: " + contacts[name])

    elif n == 2:
        print("\nadd new contacts:")
        while True:
            count = input("Enter qty of new contacts to add: ")
            try:
                count = abs(int(count))
                break
            except:
                print("\n\tERROR! Enter int. value\n")
                continue

        ind: int = 0
        while ind < count:
            print("\n" + str(ind+1) + " contact:")
            name_add = input("\tenter name\t-> ")

            while True: # check if number in digit format
                logic = False
                mob_num = input("\tenter mob.num\t-> ")
                if not mob_num[0].isdigit() and mob_num[0] != '+':
                    print("\n\tERROR!\n\tenter mob. number in format\n\t+...int digit\n\tor in 000...int digit\n")
                    continue
                else:
                    ind2: int = 1
                    while ind2 < len(mob_num):
                        if mob_num[ind2].isdigit() or mob_num[ind2] == '-':
                            ind2 += 1
                        else:
                            print("\n\tERROR!\n\tenter mob. number in format of digit number\n")
                            logic = True
                            break
                    else:
                        if mob_num[len(mob_num) - 1] == '-':
                            temp = mob_num[0:len(mob_num) - 1]
                            mob_num = temp
                        contacts[name_add] = mob_num

                if logic:
                    continue
                else:
                    ind += 1
                    break

    elif n == 3:
        print("\ndelete contacts")
        while True:
            count = input("Enter qty of contacts to delete: ")
            try:
                count = abs(int(count))
                break
            except:
                print("\n\tERROR! Enter int. value\n")
                continue

        if count > len(contacts):
            print("\nAll CONCTACTS DELETED!")
            contacts.clear()
            print("List of contacts is empty", contacts)
            break
        else:
            while count:
                name_del = input("\tenter name: ")
                if contacts.get(name_del, False):
                    del contacts[name_del]
                    print("\"{}\" contact is deleted".format(name_del))
                    count -= 1
                else:
                    print("\"{}\" is absent in contacts".format(name_del))
                    continue
    elif n == 4:
        print("\nmodify contacts")
        while True:
            name_search = input("\tenter name: ")
            if contacts.get(name_search, False):
                print("name {} : phone {}".format(name_search, contacts[name_search]))
                name_modify = input("\n\tenter new name\t-> ")
                contacts[name_modify] = contacts.pop(name_search)

                while True:  # check if number in digit format
                    logic = False
                    mobil_modify = input("\tenter new mobile -> ")
                    if not mobil_modify[0].isdigit() and mobil_modify[0] != '+':
                        print("\n\tERROR!\n\tenter mob. number in format\n\t+...int digit\n\tor in 000...int digit\n")
                        continue
                    else:
                        ind2: int = 1
                        while ind2 < len(mobil_modify):
                            if mobil_modify[ind2].isdigit() or mobil_modify[ind2] == '-':
                                ind2 += 1
                            else:
                                print("\n\tERROR!\n\tenter mob. number in format of digit number\n")
                                logic = True
                                break
                        else:
                            if mobil_modify[len(mobil_modify)-1] == '-':
                                temp = mobil_modify[0:len(mobil_modify)-1]
                                mobil_modify = temp
                            contacts[name_modify] = mobil_modify
                    if logic:
                        continue
                    else:
                        break
            else:
                print("\"{}\" is absent in contacts".format(name_search))
                continue

            ind3 = abs(int(input("\n0 - STOP! / 1 - CONTINUE\n\tenter -> ")))
            if ind3:
                continue
            else:
                print("END of SEARCH!")
                break

    elif n == 5:
        print("\nsearch contacts")
        while True:
            name_search = input("\tenter name: ")
            if contacts.get(name_search, False):
                print("name {} : phone {}".format(name_search, contacts[name_search]))
            else:
                print("\"{}\" is absent in contacts".format(name_search))
                continue
            ind3 = abs(int(input("\n0 - STOP! / 1 - CONTINUE\n\tenter -> ")))

            if ind3:
                continue
            else:
                print("END of SEARCH!")
                break