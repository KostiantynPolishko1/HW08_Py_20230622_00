
#Data
contacts = {"Kostiantyn": {"mob": "+38-073-340-90-97", "home": "+38-056-790-53-45", "work": "+38-044-750-23-40"},
            "Margarita": ["+38-096-835-60-27", "+38-096-440-19-46"],
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

    if n == 0: # EXIT
        print("\n\tEXIT!")
        break

    elif n == 1: # SHOW CONTACTS
        print("\n\tList of contacts", end='')
        if not len(contacts):
            print(" is empty", contacts)
        else:
            print(":")
            for name in contacts:
                if type(contacts[name]) == dict:
                    print(name, ":")
                    for ph in contacts[name]:
                        print("\t\t", ph, " -> ", contacts[name][ph])
                elif type(contacts[name]) == list:
                    ind = 0
                    print(name, ":")
                    for ph in contacts[name]:
                        ind += 1
                        print("\t\t phone {} -> {}".format(ind, ph))
                else:
                    print(name, " : ", contacts[name])

    elif n == 2: # ADD NEW CONTACTS
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

    elif n == 3: # DELETE CONTACTS
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
                    if type(contacts[name_del]) == dict:
                        print(name_del, ":")
                        for ph in contacts[name_del]:
                            print("\t\t", ph, " -> ", contacts[name_del][ph])
                        while True:
                            ph_type = input("enter type phone -> ")
                            if contacts[name_del].get(ph_type, False):
                                print("DELETE! ->", end='')
                                print(ph_type, " : ", contacts[name_del][ph_type])
                                del contacts[name_del][ph_type]
                                break
                            else:
                                print("enter correct type as:")
                                for i in contacts[name_del]:
                                    print("\t\t\t", i)
                                continue
                    elif type(contacts[name_del]) == list:
                        ph_pos: int = 0
                        print(name_del, ":")
                        for ind in contacts[name_del]:
                            ph_pos += 1
                            print("\t\t", ph_pos, " -> ", ind)
                        while True:
                            ph_num = int(input("enter phone Pos. delete -> "))
                            if ph_num > ph_pos:
                                print("\nN phone is out of range")
                                continue
                            print("DELETE! -> phone {}: {}".format(ph_num, contacts[name_del][ph_num-1]))
                            del contacts[name_del][ph_num-1]
                            break
                    else:
                        del contacts[name_del]
                        print("\"{}\" contact is deleted".format(name_del))
                    count -= 1
                else:
                    print("\"{}\" is absent in contacts".format(name_del))
                    continue
            else:
                print("DONE!")

    elif n == 4: # MODIFY CONTACTS
        print("\nmodify contacts")
        while True:
            ph_pos = 0
            name_search = input("\tenter name: ")
            if contacts.get(name_search, False):
                if type(contacts[name_search]) == dict:
                    print(name_search, ":")
                    for ph in contacts[name_search]:
                        print("\t\t", ph, " -> ", contacts[name_search][ph])
                elif type(contacts[name_search]) == list:
                    print(name_search, ":")
                    for ph in contacts[name_search]:
                        ph_pos += 1
                        print("\t\t phone {} -> {}".format(ph_pos, ph))
                else:
                    print("name {} : phone {}".format(name_search, contacts[name_search]))

                name_modify = input("\n\tenter new name\t-> ")
                contacts[name_modify] = contacts.pop(name_search) # new key
                print("\tNAME MODIFIED!")

                # select type of phone from dict or phone number from the list
                ph_type: str = ""
                ph_num: int = 0
                if type(contacts[name_modify]) == dict:
                    while True:
                        ph_type = input("enter type phone -> ")
                        if contacts[name_modify].get(ph_type, False):
                            print("MODIFY! ->", end = '')
                            print(ph_type, " : ", contacts[name_modify][ph_type])
                            break
                        else:
                            print("enter correct type as:")
                            for i in contacts[name_modify]:
                                print("\t\t\t", i)
                            continue
                elif type(contacts[name_modify]) == list:
                    while True:
                        ph_num = int(input("enter phone Pos. modify -> "))
                        if ph_num > ph_pos:
                            print("\nN phone is out of range")
                            continue
                        ph_num -= 1
                        print("MODIFY! -> ph: ", contacts[name_modify][ph_num])
                        break

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
                            print("\tPHONE MODIFIED!")

                    if logic:
                        continue
                    else:
                        if type(contacts[name_modify]) == dict:
                            contacts[name_modify][ph_type] = mobil_modify
                        elif type(contacts[name_modify]) == list:
                            contacts[name_modify][ph_num] = mobil_modify
                        else:
                            contacts[name_modify] = mobil_modify
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

    elif n == 5: # SEARCH CONTACTS
        print("\nsearch contacts")
        while True:
            name_search = input("\tenter name: ")
            if contacts.get(name_search, False):
                if type(contacts[name_search]) == dict:
                    print(name_search, ":")
                    for ph in contacts[name_search]:
                        print("\t\t", ph, " -> ", contacts[name_search][ph])
                elif type(contacts[name_search]) == list:
                    print(name_search, ":")
                    for ph in contacts[name_search]:
                        print("\t\t phone -> ", ph)
                else:
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