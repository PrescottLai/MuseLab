import random


def Random():
    Random_Num = random.randint(1, 9)
    if Random_Num == 1 or Random_Num == 2 or Random_Num == 3:
        Random_Num = 3
    if Random_Num == 4 or Random_Num == 5:
        Random_Num = 5
    if Random_Num == 6 or Random_Num == 7:
        Random_Num = 6
    if Random_Num == 8 or Random_Num == 9:
        Random_Num = 8
    return Random_Num


def get_cur_note_no(SolFa_List, i):
    list1 = SolFa_List
    if list1[7][i] == 1:
        x = list1[7][:i].count(1)  # counts number of 1's inside from start to i
        print("val: ", x)
        return list1[0][x]
    elif list1[7][i] == 2:
        x = list1[7][:i].count(2)
        print("val: ", x)
        return list1[1][x]
    elif list1[7][i] == 3:
        x = list1[7][:i].count(3)
        print("val: ", x)
        return list1[2][x]
    elif list1[7][i] == 4:
        x = list1[7][:i].count(4)
        print("val: ", x)
        return list1[3][x]
    elif list1[7][i] == 5:
        x = list1[7][:i].count(5)
        print("val: ", x)
        return list1[4][x]
    elif list1[7][i] == 6:
        x = list1[7][:i].count(6)
        print("val: ", x)
        return list1[5][x]
    elif list1[7][i] == 7:
        x = list1[7][:i].count(7)
        print("val: ", x)
        return list1[6][x]


def Leading_Tone(note_list, SolFa_list):
    List1 = note_list
    List2 = SolFa_list

    i = len(List1[0]) - 4
    F = note_list[0][i]
    # print("HALO")
    # print(List1[0][i])
    if List2[7][i] == 1:
        if int(List1[0][i] / 12) - 1 == 3:
            List1[0][i] -= 1
        elif int(List1[0][i] / 12) - 1 == 4:
            List1[0][i] -= 13
        elif int(List1[0][i] / 12) - 1 == 5:
            List1[0][i] -= 25
        elif int(List1[0][i] / 12) - 1 == 6:
            List1[0][i] -= 37
        elif int(List1[0][i] / 12) - 1 == 7:
            List1[0][i] -= 49
        elif int(List1[0][i] / 12) - 1 == 8:
            List1[0][i] -= 61

    elif List2[7][i] == 2:
        if int(List1[0][i] / 12) - 1 == 3:
            List1[0][i] -= 3
        elif int(List1[0][i] / 12) - 1 == 4:
            List1[0][i] -= 15
        elif int(List1[0][i] / 12) - 1 == 5:
            List1[0][i] -= 27
        elif int(List1[0][i] / 12) - 1 == 6:
            List1[0][i] -= 39
        elif int(List1[0][i] / 12) - 1 == 7:
            List1[0][i] -= 51
        elif int(List1[0][i] / 12) - 1 == 8:
            List1[0][i] -= 63

    elif List2[7][i] == 3:
        if int(List1[0][i] / 12) - 1 == 3:
            List1[0][i] -= 5
        elif int(List1[0][i] / 12) - 1 == 4:
            List1[0][i] -= 17
        elif int(List1[0][i] / 12) - 1 == 5:
            List1[0][i] -= 29
        elif int(List1[0][i] / 12) - 1 == 6:
            List1[0][i] -= 41
        elif int(List1[0][i] / 12) - 1 == 7:
            List1[0][i] -= 53
        elif int(List1[0][i] / 12) - 1 == 8:
            List1[0][i] -= 65

    elif List2[7][i] == 4:
        if int(List1[0][i] / 12) - 1 == 4:
            List1[0][i] -= 6
        elif int(List1[0][i] / 12) - 1 == 5:
            List1[0][i] -= 18
        elif int(List1[0][i] / 12) - 1 == 6:
            List1[0][i] -= 30
        elif int(List1[0][i] / 12) - 1 == 7:
            List1[0][i] -= 42
        elif int(List1[0][i] / 12) - 1 == 8:
            List1[0][i] -= 54

    elif List2[7][i] == 5:
        if int(List1[0][i] / 12) - 1 == 4:
            List1[0][i] -= 8
        elif int(List1[0][i] / 12) - 1 == 5:
            List1[0][i] -= 20
        elif int(List1[0][i] / 12) - 1 == 6:
            List1[0][i] -= 32
        elif int(List1[0][i] / 12) - 1 == 7:
            List1[0][i] -= 44
        elif int(List1[0][i] / 12) - 1 == 8:
            List1[0][i] -= 56

    elif List2[7][i] == 6:
        if int(List1[0][i] / 12) - 1 == 4:
            List1[0][i] -= 10
        elif int(List1[0][i] / 12) - 1 == 5:
            List1[0][i] -= 22
        elif int(List1[0][i] / 12) - 1 == 6:
            List1[0][i] -= 34
        elif int(List1[0][i] / 12) - 1 == 7:
            List1[0][i] -= 46
        elif int(List1[0][i] / 12) - 1 == 8:
            List1[0][i] -= 58

    elif List2[7][i] == 7:
        if int(List1[0][i] / 12) - 1 == 4:
            List1[0][i] -= 12
        elif int(List1[0][i] / 12) - 1 == 5:
            List1[0][i] -= 24
        elif int(List1[0][i] / 12) - 1 == 6:
            List1[0][i] -= 36
        elif int(List1[0][i] / 12) - 1 == 7:
            List1[0][i] -= 48
        elif int(List1[0][i] / 12) - 1 == 8:
            List1[0][i] -= 60

    Leading_Num = List1[0][i]
    note_list[0][i] = F
    return Leading_Num
