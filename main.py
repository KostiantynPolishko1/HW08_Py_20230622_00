
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
            print("\n\tERROR!" + str(n) + "is out of range 0...6\n")
            continue
    except:
        print("\n\tERROR! Enter int. value\n")
        continue
    print("\t\toperation", n)

    if n == 0:
        print("\n\tEXIT!")
        break

    elif n == 1:
        print("\n\tList of contacts:")
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
            name = input("\tenter name\t-> ")

            while True: # check if number in digit format
                logic = False
                mob_num = input("\tenter mob.num\t-> ")
                if not mob_num[0].isdigit() and mob_num[0] != "+":
                    print("\n\tERROR!\n\tenter mob. number in format\n\t+...int digit\n\tor in 000...int digit\n")
                    continue
                else:
                    ind2: int = 1
                    while ind2 < len(mob_num):
                        if not (mob_num[ind2].isdigit()):
                            print("\n\tERROR!\n\tenter mob. number in format of digit number\n")
                            logic = True
                            break
                        ind2 += 1
                    else:
                        contacts[name] = mob_num

                if logic:
                    continue
                else:
                    ind += 1
                    break
