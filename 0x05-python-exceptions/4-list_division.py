#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divlist = []
    i = 0
    div = 0
    while True:
        try:
            if (i < list_length):
                div = my_list_1[i]/my_list_2[i]
                i += 1
            else:
                break
        except TypeError:
            div = 0
            print("wrong type")
            i += 1
        except ZeroDivisionError:
            div = 0
            print("division by zero")
            i += 1
        except IndexError:
            div = 0
            print("out of range")
            break
        finally:
            divlist.append(div)
    return(divlist)
