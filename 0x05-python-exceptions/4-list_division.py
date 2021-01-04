#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divlist = []
    i = 0
    div = 0
    while True:
        try:
            if (i < list_length):
                div = my_list_1[i]/my_list_2[i]
                divlist.append(div)
            else:
                break
            i += 1
        except TypeError:
            divlist.append(0)
            print("wrong type")
            i += 1
        except ZeroDivisionError:
            divlist.append(0)
            print("division by zero")
            i += 1
        except IndexError:
            divlist.append(0)
            print("out of range")
            break
    return(divlist)
