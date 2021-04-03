import os
from Add_BaseChord import *
from Functions import *
from mido import MetaMessage
import platform

system_name = platform.system()
print(system_name)
if system_name == 'Windows':
    import win32api


def melody_generate(file_path):
    s = converter.parse(file_path)
    mid = MidiFile(file_path)
    s.write("midi", "./music/Output/Input.mid")
    k = 'Key'
    z = 0
    Tempo = 10000
    list_c, list_n, list_v, list_t, channel_list, note_list, velocity_list, time_list = \
        [], [], [], [], [], [], [], []
    print("Input_mid_Info: ", mid)
    # -----------Grab the useful message from original midi file, Note number, Key, Key signature, Tempo --------
    for i in range(len(mid.tracks)):
        for msg in mid.tracks[i]:
            if msg.type == 'note_on' or msg.type == 'note_off':
                list_c.append(msg.channel)
                list_n.append(msg.note)
                list_v.append(msg.velocity)
                list_t.append(msg.time)
                z += 1
            if msg.type == 'key_signature':
                k = msg.key
                print(k)
            if msg.type == 'set_tempo':
                Tempo = msg.tempo
            print("Input_msg: ", z, msg)  # debug
            # C-A(m3),D-B(m3),E-C(M3),F-D(m3),G-E(m3),A-F(M3),B-G(M3) m3: -3 M3:-4
        i += 1
        note_list.append(list_n)
        channel_list.append(list_c)
        velocity_list.append(list_v)
        time_list.append(list_t)

    melody_key = s.analyze('key')
    melody_key.tonic.name = k
    print("Input key:", melody_key.tonic.name, melody_key.mode)
    print("Melody_Tempo:", Tempo)

    # ---------------Create Lists of intervals 3rd & 5th & 6th & 8ve------------------
    Note_SolFaNameList3rd = Get_SolFa_Name_Order(file_path)
    Note_SolFaNameList5th = Get_SolFa_Name_Order(file_path)
    Note_SolFaNameList8ve = Get_SolFa_Name_Order(file_path)
    Note_SolFaNameList6th = Get_SolFa_Name_Order(file_path)
    SolFa_List = Get_SolFa_Name_Order(file_path)
    CounterMelody_List, FinalOrder_list5th = [], []

    for i in range(len(Note_SolFaNameList3rd)):
        j = 0
        k = 0
        y = 0
        x = 0
        while j < len(Note_SolFaNameList3rd[i]):
            if melody_key.mode == 'major':
                if i == 0 or i == 1 or i == 3 or i == 4:
                    if (int(Note_SolFaNameList3rd[i][j] / 12) - 1) <= 4:
                        Note_SolFaNameList3rd[i][j] -= 3
                    elif (int(Note_SolFaNameList3rd[i][j] / 12) - 1) == 5:
                        Note_SolFaNameList3rd[i][j] -= 15
                    elif (int(Note_SolFaNameList3rd[i][j] / 12) - 1) == 6:
                        Note_SolFaNameList3rd[i][j] -= 27
                    elif (int(Note_SolFaNameList3rd[i][j] / 12) - 1) == 7:
                        Note_SolFaNameList3rd[i][j] -= 39
                    elif (int(Note_SolFaNameList3rd[i][j] / 12) - 1) == 8:
                        Note_SolFaNameList3rd[i][j] -= 51
                if i == 2 or i == 5 or i == 6:
                    if (int(Note_SolFaNameList3rd[i][j] / 12) - 1) <= 4:
                        Note_SolFaNameList3rd[i][j] -= 4
                    elif (int(Note_SolFaNameList3rd[i][j] / 12) - 1) == 5:
                        Note_SolFaNameList3rd[i][j] -= 16
                    elif (int(Note_SolFaNameList3rd[i][j] / 12) - 1) == 6:
                        Note_SolFaNameList3rd[i][j] -= 28
                    elif (int(Note_SolFaNameList5th[i][j] / 12) - 1) == 7:
                        Note_SolFaNameList3rd[i][j] -= 40
                    elif (int(Note_SolFaNameList3rd[i][j] / 12) - 1) == 8:
                        Note_SolFaNameList3rd[i][j] -= 52
            j += 1
        while k < len(Note_SolFaNameList5th[i]):
            # print("k",k)#debug
            if melody_key.mode == 'major':
                if i == 3:
                    if (int(Note_SolFaNameList5th[i][k] / 12) - 1) <= 4:
                        Note_SolFaNameList5th[i][k] -= 6
                    elif (int(Note_SolFaNameList5th[i][k] / 12) - 1) == 5:
                        Note_SolFaNameList5th[i][k] -= 18
                    elif (int(Note_SolFaNameList5th[i][k] / 12) - 1) == 6:
                        Note_SolFaNameList5th[i][k] -= 30
                    elif (int(Note_SolFaNameList5th[i][k] / 12) - 1) == 7:
                        Note_SolFaNameList5th[i][k] -= 42
                    elif (int(Note_SolFaNameList5th[i][k] / 12) - 1) == 8:
                        Note_SolFaNameList5th[i][k] -= 54
                else:
                    if (int(Note_SolFaNameList5th[i][k] / 12) - 1) <= 4:
                        Note_SolFaNameList5th[i][k] -= 7
                    elif (int(Note_SolFaNameList5th[i][k] / 12) - 1) == 5:
                        Note_SolFaNameList5th[i][k] -= 19
                    elif (int(Note_SolFaNameList5th[i][k] / 12) - 1) == 6:
                        Note_SolFaNameList5th[i][k] -= 31
                    elif (int(Note_SolFaNameList5th[i][k] / 12) - 1) == 7:
                        Note_SolFaNameList5th[i][k] -= 43
                    elif (int(Note_SolFaNameList5th[i][k] / 12) - 1) == 8:
                        Note_SolFaNameList5th[i][k] -= 55
            k += 1
        while x < len(Note_SolFaNameList8ve[i]):
            Note_SolFaNameList8ve[i][x] -= 12
            x += 1
        while y < len(Note_SolFaNameList6th[i]):

            if melody_key.mode == 'major':
                if i == 0 or i == 3 or i == 4:
                    if (int(Note_SolFaNameList6th[i][y] / 12) - 1) <= 4:
                        Note_SolFaNameList6th[i][y] -= 8
                    elif (int(Note_SolFaNameList6th[i][y] / 12) - 1) == 5:
                        Note_SolFaNameList6th[i][y] -= 20
                    elif (int(Note_SolFaNameList6th[i][y] / 12) - 1) == 6:
                        Note_SolFaNameList6th[i][y] -= 32
                    elif (int(Note_SolFaNameList6th[i][y] / 12) - 1) == 7:
                        Note_SolFaNameList6th[i][y] -= 44
                    elif (int(Note_SolFaNameList6th[i][y] / 12) - 1) == 8:
                        Note_SolFaNameList6th[i][y] -= 56
                else:
                    if (int(Note_SolFaNameList6th[i][y] / 12) - 1) <= 4:
                        Note_SolFaNameList6th[i][y] -= 9
                    elif (int(Note_SolFaNameList6th[i][y] / 12) - 1) == 5:
                        Note_SolFaNameList6th[i][y] -= 21
                    elif (int(Note_SolFaNameList6th[i][y] / 12) - 1) == 6:
                        Note_SolFaNameList6th[i][y] -= 33
                    elif (int(Note_SolFaNameList6th[i][y] / 12) - 1) == 7:
                        Note_SolFaNameList6th[i][y] -= 45
                    elif (int(Note_SolFaNameList6th[i][y] / 12) - 1) == 8:
                        Note_SolFaNameList6th[i][y] -= 57
            y += 1

    # ---------------------------------Generate the Counter melody part----------------------------------------
    needed_num = 0
    prev_note_num = 0  # previous MIDI number
    diff_check = []  # checks difference between current counter notes and previous counter notes(NOT simply notes!)
    prev_c_num = 0  # previous counter MIDI number

    # print(len(Note_SolFaNameList3rd[7])) #debug
    # print(SolFa_List) #debug
    # print("Time list: ", time_list[0])
    # print("Note list: ", note_list[0])

    # loops
    L_note_3rd = []
    print("Generating Alto/Counter Melody......")
    for i in range(len(Note_SolFaNameList3rd[7])):
        # print("i_Number: ", i)#debug
        cur_note_num = get_cur_note_no(SolFa_List, i)  # gets the current Input MIDI number with function
        # print("Current_Note_Num:")#debug
        # print(cur_note_num)#debug
        # print("SolFa_Name:")#debug
        # print(Note_SolFaNameList3rd[7][i])#debug

        if Note_SolFaNameList3rd[7][i] == 1:
            # print("flag")#debug

            Note_3rd = Note_SolFaNameList3rd[0].pop(0)
            Note_5th = Note_SolFaNameList5th[0].pop(0)
            Note_6th = Note_SolFaNameList6th[0].pop(0)
            Note_8ve = Note_SolFaNameList8ve[0].pop(0)
            print("intervals:")  # debug
            print(Note_3rd, Note_5th, Note_6th, Note_8ve)  # debug
            print("Previous_C_Num:")  # debug
            print(prev_c_num)  # debug
            L_note_3rd.append(Note_3rd)
            if i == len(Note_SolFaNameList3rd[7]) - 2 or i == len(Note_SolFaNameList3rd[7]) - 1:  # The last note
                CounterMelody_List.append(Note_8ve)
                FinalOrder_list5th.append(Note_5th)
                continue
            # below is list for recording val. diff. of each chord(3,5,6,8), also in such order
            diff_check.append(int(Note_3rd - prev_c_num))
            diff_check.append(int(Note_5th - prev_c_num))
            diff_check.append(int(Note_6th - prev_c_num))
            diff_check.append(int(Note_8ve - prev_c_num))
            # print(diff_check)#debug
            # print(i)

            if i > 1:
                if cur_note_num > prev_note_num:  # Input melody ascending, need -ve notes for counter
                    # print("Currently ascending!") #debug
                    if min(diff_check) < 0:
                        if any(-3 <= elem < 0 for elem in diff_check):
                            needed_num = diff_check.index(max([no for no in diff_check if no < 0]))
                        else:
                            needed_num = diff_check.index(max([no for no in diff_check if no <= 0]))
                        # print("Flag")
                    else:
                        Note_8ve -= 12
                        Note_6th -= 12
                        Note_5th -= 12
                        Note_3rd -= 12
                        diff_check[0] = (int(Note_3rd - prev_c_num))
                        diff_check[1] = (int(Note_5th - prev_c_num))
                        diff_check[2] = (int(Note_6th - prev_c_num))
                        diff_check[3] = (int(Note_8ve - prev_c_num))
                        print(diff_check)
                        if any(-3 <= elem < 0 for elem in diff_check):
                            needed_num = diff_check.index(max([no for no in diff_check if no < 0]))
                        else:
                            needed_num = diff_check.index(max([no for no in diff_check if no <= 0]))
                else:  # descending, need +ve notes for counter
                    # print("Currently descending!")#debug
                    if max(diff_check) >= 0:
                        if any(3 >= elem > 0 for elem in diff_check):
                            needed_num = diff_check.index(min([no for no in diff_check if no > 0]))
                        else:
                            needed_num = diff_check.index(min([no for no in diff_check if no >= 0]))
                        # print("Flag")
                    else:
                        Note_8ve += 12
                        Note_6th += 12
                        Note_5th += 12
                        Note_3rd += 12
                        diff_check[0] = (int(Note_3rd - prev_c_num))
                        diff_check[1] = (int(Note_5th - prev_c_num))
                        diff_check[2] = (int(Note_6th - prev_c_num))
                        diff_check[3] = (int(Note_8ve - prev_c_num))
                        print(diff_check)
                        if any(3 >= elem > 0 for elem in diff_check):
                            needed_num = diff_check.index(min([no for no in diff_check if no > 0]))
                        else:
                            needed_num = diff_check.index(min([no for no in diff_check if no >= 0]))
                        # print("Flag")
                print("needed_num: ", needed_num)  # debug
                # print(i)
                # print("\n")

            FinalOrder_list5th.append(Note_5th)
            if i == 0 or i == 1:
                prev_c_num = Note_8ve  # update previous counter melody note num.
                CounterMelody_List.append(Note_8ve)
                # print("flag2")
                # print(prev_c_num)
            if i == len(Note_SolFaNameList3rd[7]) - 4 or i == len(Note_SolFaNameList3rd[7]) - 3:
                if melody_key.mode == 'major' and \
                        (melody_key.tonic.name == 'G' or melody_key.tonic.name == 'A' or melody_key.tonic.name == 'D'):
                    Leading_Num = Leading_Tone(note_list, SolFa_List)
                    CounterMelody_List.append(Leading_Num)
                else:
                    if needed_num == 0:  #
                        CounterMelody_List.append(Note_3rd)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 1:
                        CounterMelody_List.append(Note_5th)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 2:
                        CounterMelody_List.append(Note_6th)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 3:
                        CounterMelody_List.append(Note_8ve)
                        prev_c_num = CounterMelody_List[i - 1]

            if needed_num == 0 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:  # Normal cases
                CounterMelody_List.append(Note_3rd)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 1 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_5th)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 2 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_6th)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 3 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_8ve)
                prev_c_num = CounterMelody_List[i - 1]

                # print(CounterMelody_List[i])
            # print(CounterMelody_List[i])

        if Note_SolFaNameList3rd[7][i] == 2:
            Note_3rd = Note_SolFaNameList3rd[1].pop(0)
            Note_5th = Note_SolFaNameList5th[1].pop(0)
            Note_8ve = Note_SolFaNameList8ve[1].pop(0)
            Note_6th = Note_SolFaNameList6th[1].pop(0)
            print("intervals:")
            print(Note_3rd, Note_5th, Note_6th, Note_8ve)
            print("Previous_C_Num:")
            print(prev_c_num)
            L_note_3rd.append(Note_3rd)
            if i == len(Note_SolFaNameList3rd[7]) - 2 or i == len(Note_SolFaNameList3rd[7]) - 1:  # The last note
                CounterMelody_List.append(Note_8ve)
                FinalOrder_list5th.append(Note_5th)
                continue

            diff_check.append(Note_3rd - prev_c_num)
            diff_check.append(Note_5th - prev_c_num)
            diff_check.append(Note_6th - prev_c_num)
            diff_check.append(Note_8ve - prev_c_num)
            print(diff_check)

            if i > 1:
                # print("Flag")
                if cur_note_num > prev_note_num:  # ascending, need -ve notes for counter
                    print("Currently ascending!")
                    if min(diff_check) <= 0:
                        if any(-3 <= elem < 0 for elem in diff_check):
                            needed_num = diff_check.index(max([no for no in diff_check if no < 0]))
                        else:
                            needed_num = diff_check.index(max([no for no in diff_check if no <= 0]))
                        # print("Flag")
                    else:
                        Note_8ve -= 12
                        Note_6th -= 12
                        Note_5th -= 12
                        Note_3rd -= 12
                        diff_check[0] = (int(Note_3rd - prev_c_num))
                        diff_check[1] = (int(Note_5th - prev_c_num))
                        diff_check[2] = (int(Note_6th - prev_c_num))
                        diff_check[3] = (int(Note_8ve - prev_c_num))
                        print(diff_check)
                        if any(-3 <= elem < 0 for elem in diff_check):
                            needed_num = diff_check.index(max([no for no in diff_check if no < 0]))
                        else:
                            needed_num = diff_check.index(max([no for no in diff_check if no <= 0]))
                else:  # descending, need +ve notes for counter
                    print("Currently descending!")
                    if max(diff_check) >= 0:
                        if any(3 >= elem > 0 for elem in diff_check):
                            needed_num = diff_check.index(min([no for no in diff_check if no > 0]))
                        else:
                            needed_num = diff_check.index(min([no for no in diff_check if no >= 0]))
                        # print("Flag")
                    else:
                        Note_8ve += 12
                        Note_6th += 12
                        Note_5th += 12
                        Note_3rd += 12
                        diff_check[0] = (int(Note_3rd - prev_c_num))
                        diff_check[1] = (int(Note_5th - prev_c_num))
                        diff_check[2] = (int(Note_6th - prev_c_num))
                        diff_check[3] = (int(Note_8ve - prev_c_num))
                        print(diff_check)
                        if any(3 >= elem > 0 for elem in diff_check):
                            needed_num = diff_check.index(min([no for no in diff_check if no > 0]))
                        else:
                            needed_num = diff_check.index(min([no for no in diff_check if no >= 0]))
                        # print("Flag")
                print("needed_num: ", needed_num)

            FinalOrder_list5th.append(Note_5th)
            if i == 0 or i == 1:
                prev_c_num = Note_8ve
                CounterMelody_List.append(Note_8ve)
            if i == len(Note_SolFaNameList3rd[7]) - 4 or i == len(Note_SolFaNameList3rd[7]) - 3:
                if melody_key.mode == 'major' and \
                        (melody_key.tonic.name == 'G' or melody_key.tonic.name == 'A' or melody_key.tonic.name == 'D'):
                    Leading_Num = Leading_Tone(note_list, SolFa_List)
                    CounterMelody_List.append(Leading_Num)
                else:
                    if needed_num == 0:  #
                        CounterMelody_List.append(Note_3rd)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 1:
                        CounterMelody_List.append(Note_5th)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 2:
                        CounterMelody_List.append(Note_6th)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 3:
                        CounterMelody_List.append(Note_8ve)
                        prev_c_num = CounterMelody_List[i - 1]

            if needed_num == 0 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:  # Normal cases
                CounterMelody_List.append(Note_3rd)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 1 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_5th)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 2 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_6th)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 3 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_8ve)
                prev_c_num = CounterMelody_List[i - 1]

        if Note_SolFaNameList3rd[7][i] == 3:
            print("!!!!!!!!!!!!!!!!!!!!!!")
            Note_3rd = Note_SolFaNameList3rd[2].pop(0)
            Note_5th = Note_SolFaNameList5th[2].pop(0)
            Note_8ve = Note_SolFaNameList8ve[2].pop(0)
            Note_6th = Note_SolFaNameList6th[2].pop(0)
            print("intervals:")
            print(Note_3rd, Note_5th, Note_6th, Note_8ve)
            print("Previous_C_Num:")
            print(prev_c_num)
            L_note_3rd.append(Note_3rd)
            if i == len(Note_SolFaNameList3rd[7]) - 2 or i == len(Note_SolFaNameList3rd[7]) - 1:  # The last note
                CounterMelody_List.append(Note_8ve)
                FinalOrder_list5th.append(Note_5th)
                continue

            diff_check.append(Note_3rd - prev_c_num)
            diff_check.append(Note_5th - prev_c_num)
            diff_check.append(Note_6th - prev_c_num)
            diff_check.append(Note_8ve - prev_c_num)
            print(diff_check)

            if i > 1:
                # print("Flag")
                if cur_note_num > prev_note_num:  # ascending, need -ve notes for counter
                    print("Currently ascending!")
                    if min(diff_check) < 0:
                        if min(diff_check) <= 0:
                            if any(-3 <= elem < 0 for elem in diff_check):
                                needed_num = diff_check.index(max([no for no in diff_check if no < 0]))
                            else:
                                needed_num = diff_check.index(max([no for no in diff_check if no <= 0]))
                        # print("Flag")
                    else:
                        Note_8ve -= 12
                        Note_6th -= 12
                        Note_5th -= 12
                        Note_3rd -= 12
                        diff_check[0] = (int(Note_3rd - prev_c_num))
                        diff_check[1] = (int(Note_5th - prev_c_num))
                        diff_check[2] = (int(Note_6th - prev_c_num))
                        diff_check[3] = (int(Note_8ve - prev_c_num))
                        print(diff_check)
                        if min(diff_check) <= 0:
                            if any(-3 <= elem < 0 for elem in diff_check):
                                needed_num = diff_check.index(max([no for no in diff_check if no < 0]))
                            else:
                                needed_num = diff_check.index(max([no for no in diff_check if no <= 0]))
                else:  # descending, need +ve notes for counter
                    print("Currently descending!")
                    if max(diff_check) >= 0:
                        if any(3 >= elem > 0 for elem in diff_check):
                            needed_num = diff_check.index(min([no for no in diff_check if no > 0]))
                        else:
                            needed_num = diff_check.index(min([no for no in diff_check if no >= 0]))
                        # print("Flag")
                    else:
                        Note_8ve += 12
                        Note_6th += 12
                        Note_5th += 12
                        Note_3rd += 12
                        diff_check[0] = (int(Note_3rd - prev_c_num))
                        diff_check[1] = (int(Note_5th - prev_c_num))
                        diff_check[2] = (int(Note_6th - prev_c_num))
                        diff_check[3] = (int(Note_8ve - prev_c_num))
                        print(diff_check)
                        if any(3 >= elem > 0 for elem in diff_check):
                            needed_num = diff_check.index(min([no for no in diff_check if no > 0]))
                        else:
                            needed_num = diff_check.index(min([no for no in diff_check if no >= 0]))
                        # print("Flag")
                print("needed_num: ", needed_num)

            FinalOrder_list5th.append(Note_5th)
            if i == 0 or i == 1:
                prev_c_num = Note_8ve
                CounterMelody_List.append(Note_8ve)
            if i == len(Note_SolFaNameList3rd[7]) - 4 or i == len(Note_SolFaNameList3rd[7]) - 3:
                if melody_key.mode == 'major' and \
                        (melody_key.tonic.name == 'G' or melody_key.tonic.name == 'A' or melody_key.tonic.name == 'D'):
                    Leading_Num = Leading_Tone(note_list, SolFa_List)
                    CounterMelody_List.append(Leading_Num)
                else:
                    if needed_num == 0:  #
                        CounterMelody_List.append(Note_3rd)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 1:
                        CounterMelody_List.append(Note_5th)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 2:
                        CounterMelody_List.append(Note_6th)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 3:
                        CounterMelody_List.append(Note_8ve)
                        prev_c_num = CounterMelody_List[i - 1]

            if needed_num == 0 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:  # Normal cases
                print("______________")
                print(CounterMelody_List[i - 1])
                CounterMelody_List.append(Note_3rd)
                prev_c_num = CounterMelody_List[i - 1]
                print(prev_c_num)
            if needed_num == 1 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_5th)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 2 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_6th)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 3 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_8ve)
                prev_c_num = CounterMelody_List[i - 1]

        if Note_SolFaNameList3rd[7][i] == 4:
            Note_3rd = Note_SolFaNameList3rd[3].pop(0)
            Note_5th = Note_SolFaNameList5th[3].pop(0)
            Note_8ve = Note_SolFaNameList8ve[3].pop(0)
            Note_6th = Note_SolFaNameList6th[3].pop(0)
            print("intervals:")
            print(Note_3rd, Note_5th, Note_6th, Note_8ve)
            print("Previous_C_Num:")
            print(prev_c_num)
            L_note_3rd.append(Note_3rd)
            if i == len(Note_SolFaNameList3rd[7]) - 2 or i == len(Note_SolFaNameList3rd[7]) - 1:  # The last note
                CounterMelody_List.append(Note_8ve)
                FinalOrder_list5th.append(Note_5th)
                continue

            diff_check.append(Note_3rd - prev_c_num)
            diff_check.append(Note_5th - prev_c_num)
            diff_check.append(Note_6th - prev_c_num)
            diff_check.append(Note_8ve - prev_c_num)
            print(diff_check)

            if i > 1:
                # print("Flag")
                if cur_note_num > prev_note_num:  # ascending, need -ve notes for counter
                    print("Currently ascending!")
                    if min(diff_check) < 0:
                        if any(-3 <= elem < 0 for elem in diff_check):
                            needed_num = diff_check.index(max([no for no in diff_check if no < 0]))
                        else:
                            needed_num = diff_check.index(max([no for no in diff_check if no <= 0]))
                        # print("Flag")
                    else:
                        Note_8ve -= 12
                        Note_6th -= 12
                        Note_5th -= 12
                        Note_3rd -= 12
                        diff_check[0] = (int(Note_3rd - prev_c_num))
                        diff_check[1] = (int(Note_5th - prev_c_num))
                        diff_check[2] = (int(Note_6th - prev_c_num))
                        diff_check[3] = (int(Note_8ve - prev_c_num))
                        print(diff_check)
                        if any(-3 <= elem < 0 for elem in diff_check):
                            needed_num = diff_check.index(max([no for no in diff_check if no < 0]))
                        else:
                            needed_num = diff_check.index(max([no for no in diff_check if no <= 0]))
                else:  # descending, need +ve notes for counter
                    print("Currently descending!")
                    if max(diff_check) >= 0:
                        if any(3 >= elem > 0 for elem in diff_check):
                            needed_num = diff_check.index(min([no for no in diff_check if no > 0]))
                        else:
                            needed_num = diff_check.index(min([no for no in diff_check if no >= 0]))
                        # print("Flag")
                    else:
                        Note_8ve += 12
                        Note_6th += 12
                        Note_5th += 12
                        Note_3rd += 12
                        diff_check[0] = (int(Note_3rd - prev_c_num))
                        diff_check[1] = (int(Note_5th - prev_c_num))
                        diff_check[2] = (int(Note_6th - prev_c_num))
                        diff_check[3] = (int(Note_8ve - prev_c_num))
                        print(diff_check)
                        if any(3 >= elem > 0 for elem in diff_check):
                            needed_num = diff_check.index(min([no for no in diff_check if no > 0]))
                        else:
                            needed_num = diff_check.index(min([no for no in diff_check if no >= 0]))
                        # print("Flag")
                print("needed_num: ", needed_num)

            FinalOrder_list5th.append(Note_5th)
            if i == 0 or i == 1:
                prev_c_num = Note_8ve
                CounterMelody_List.append(Note_8ve)
            if i == len(Note_SolFaNameList3rd[7]) - 4 or i == len(Note_SolFaNameList3rd[7]) - 3:
                if melody_key.mode == 'major' and \
                        (melody_key.tonic.name == 'G' or melody_key.tonic.name == 'A' or melody_key.tonic.name == 'D'):
                    Leading_Num = Leading_Tone(note_list, SolFa_List)
                    CounterMelody_List.append(Leading_Num)
                    print(CounterMelody_List[i])
                else:
                    if needed_num == 0:  #
                        CounterMelody_List.append(Note_3rd)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 1:
                        CounterMelody_List.append(Note_5th)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 2:
                        CounterMelody_List.append(Note_6th)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 3:
                        CounterMelody_List.append(Note_8ve)
                        prev_c_num = CounterMelody_List[i - 1]

            if needed_num == 0 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:  # Normal cases
                CounterMelody_List.append(Note_3rd)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 1 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_5th)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 2 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_6th)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 3 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_8ve)
                prev_c_num = CounterMelody_List[i - 1]

        if Note_SolFaNameList3rd[7][i] == 5:
            Note_3rd = Note_SolFaNameList3rd[4].pop(0)
            Note_5th = Note_SolFaNameList5th[4].pop(0)
            Note_8ve = Note_SolFaNameList8ve[4].pop(0)
            Note_6th = Note_SolFaNameList6th[4].pop(0)
            print("intervals:")
            print(Note_3rd, Note_5th, Note_6th, Note_8ve)
            print("Previous_C_Num:")
            print(prev_c_num)
            L_note_3rd.append(Note_3rd)
            if i == len(Note_SolFaNameList3rd[7]) - 2 or i == len(Note_SolFaNameList3rd[7]) - 1:  # The last note
                CounterMelody_List.append(Note_8ve)
                FinalOrder_list5th.append(Note_5th)
                continue

            diff_check.append(Note_3rd - prev_c_num)
            diff_check.append(Note_5th - prev_c_num)
            diff_check.append(Note_6th - prev_c_num)
            diff_check.append(Note_8ve - prev_c_num)
            print(diff_check)

            if i > 1:
                # print("Flag")
                if cur_note_num > prev_note_num:  # ascending, need -ve notes for counter
                    print("Currently ascending!")
                    if min(diff_check) < 0:
                        if any(-3 <= elem < 0 for elem in diff_check):
                            needed_num = diff_check.index(max([no for no in diff_check if no < 0]))
                        else:
                            needed_num = diff_check.index(max([no for no in diff_check if no <= 0]))
                        # print("Flag")
                    else:
                        Note_8ve -= 12
                        Note_6th -= 12
                        Note_5th -= 12
                        Note_3rd -= 12
                        diff_check[0] = (int(Note_3rd - prev_c_num))
                        diff_check[1] = (int(Note_5th - prev_c_num))
                        diff_check[2] = (int(Note_6th - prev_c_num))
                        diff_check[3] = (int(Note_8ve - prev_c_num))
                        print(diff_check)
                        if any(-3 <= elem < 0 for elem in diff_check):
                            needed_num = diff_check.index(max([no for no in diff_check if no < 0]))
                        else:
                            needed_num = diff_check.index(max([no for no in diff_check if no <= 0]))
                else:  # descending, need +ve notes for counter
                    print("Currently descending!")
                    if max(diff_check) >= 0:
                        if any(3 >= elem > 0 for elem in diff_check):
                            needed_num = diff_check.index(min([no for no in diff_check if no > 0]))
                        else:
                            needed_num = diff_check.index(min([no for no in diff_check if no >= 0]))
                        # print("Flag")
                    else:
                        Note_8ve += 12
                        Note_6th += 12
                        Note_5th += 12
                        Note_3rd += 12
                        diff_check[0] = (int(Note_3rd - prev_c_num))
                        diff_check[1] = (int(Note_5th - prev_c_num))
                        diff_check[2] = (int(Note_6th - prev_c_num))
                        diff_check[3] = (int(Note_8ve - prev_c_num))
                        print(diff_check)
                        if any(3 >= elem > 0 for elem in diff_check):
                            needed_num = diff_check.index(min([no for no in diff_check if no > 0]))
                        else:
                            needed_num = diff_check.index(min([no for no in diff_check if no >= 0]))
                        # print("Flag")
                print("needed_num: ", needed_num)

            FinalOrder_list5th.append(Note_5th)
            if i == 0 or i == 1:
                prev_c_num = Note_8ve
                CounterMelody_List.append(Note_8ve)
            if i == len(Note_SolFaNameList3rd[7]) - 4 or i == len(Note_SolFaNameList3rd[7]) - 3:
                if melody_key.mode == 'major' and \
                        (melody_key.tonic.name == 'G' or melody_key.tonic.name == 'A' or melody_key.tonic.name == 'D'):
                    Leading_Num = Leading_Tone(note_list, SolFa_List)
                    CounterMelody_List.append(Leading_Num)
                else:
                    if needed_num == 0:  #
                        CounterMelody_List.append(Note_3rd)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 1:
                        CounterMelody_List.append(Note_5th)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 2:
                        CounterMelody_List.append(Note_6th)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 3:
                        CounterMelody_List.append(Note_8ve)
                        prev_c_num = CounterMelody_List[i - 1]

            if needed_num == 0 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:  # Normal cases
                CounterMelody_List.append(Note_3rd)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 1 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_5th)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 2 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_6th)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 3 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_8ve)
                prev_c_num = CounterMelody_List[i - 1]

        if Note_SolFaNameList3rd[7][i] == 6:
            Note_3rd = Note_SolFaNameList3rd[5].pop(0)
            Note_5th = Note_SolFaNameList5th[5].pop(0)
            Note_8ve = Note_SolFaNameList8ve[5].pop(0)
            Note_6th = Note_SolFaNameList6th[5].pop(0)
            print("intervals:")
            print(Note_3rd, Note_5th, Note_6th, Note_8ve)
            print("Previous_C_Num:")
            print(prev_c_num)
            L_note_3rd.append(Note_3rd)
            if i == len(Note_SolFaNameList3rd[7]) - 2 or i == len(Note_SolFaNameList3rd[7]) - 1:  # The last note
                CounterMelody_List.append(Note_8ve)
                FinalOrder_list5th.append(Note_5th)
                continue

            diff_check.append(Note_3rd - prev_c_num)
            diff_check.append(Note_5th - prev_c_num)
            diff_check.append(Note_6th - prev_c_num)
            diff_check.append(Note_8ve - prev_c_num)
            print(diff_check)

            if i > 1:
                # print("Flag")
                if cur_note_num > prev_note_num:  # ascending, need -ve notes for counter
                    print("Currently ascending!")
                    if min(diff_check) < 0:
                        if any(-3 <= elem < 0 for elem in diff_check):
                            needed_num = diff_check.index(max([no for no in diff_check if no < 0]))
                        else:
                            needed_num = diff_check.index(max([no for no in diff_check if no <= 0]))
                        # print("Flag")
                    else:
                        Note_8ve -= 12
                        Note_6th -= 12
                        Note_5th -= 12
                        Note_3rd -= 12
                        diff_check[0] = (int(Note_3rd - prev_c_num))
                        diff_check[1] = (int(Note_5th - prev_c_num))
                        diff_check[2] = (int(Note_6th - prev_c_num))
                        diff_check[3] = (int(Note_8ve - prev_c_num))
                        print(diff_check)
                        if any(-3 <= elem < 0 for elem in diff_check):
                            needed_num = diff_check.index(max([no for no in diff_check if no < 0]))
                        else:
                            needed_num = diff_check.index(max([no for no in diff_check if no <= 0]))
                else:  # descending, need +ve notes for counter
                    print("Currently descending!")
                    if max(diff_check) >= 0:
                        if any(3 >= elem > 0 for elem in diff_check):
                            needed_num = diff_check.index(min([no for no in diff_check if no > 0]))
                        else:
                            needed_num = diff_check.index(min([no for no in diff_check if no >= 0]))
                        # print("Flag")
                    else:
                        Note_8ve += 12
                        Note_6th += 12
                        Note_5th += 12
                        Note_3rd += 12
                        diff_check[0] = (int(Note_3rd - prev_c_num))
                        diff_check[1] = (int(Note_5th - prev_c_num))
                        diff_check[2] = (int(Note_6th - prev_c_num))
                        diff_check[3] = (int(Note_8ve - prev_c_num))
                        print(diff_check)
                        if any(3 >= elem > 0 for elem in diff_check):
                            needed_num = diff_check.index(min([no for no in diff_check if no > 0]))
                        else:
                            needed_num = diff_check.index(min([no for no in diff_check if no >= 0]))
                        # print("Flag")
                print("needed_num: ", needed_num)

            FinalOrder_list5th.append(Note_5th)
            if i == 0 or i == 1:
                prev_c_num = Note_8ve
                CounterMelody_List.append(Note_8ve)

            if i == len(Note_SolFaNameList3rd[7]) - 4 or i == len(Note_SolFaNameList3rd[7]) - 3:
                if melody_key.mode == 'major' and \
                        (melody_key.tonic.name == 'G' or melody_key.tonic.name == 'A' or melody_key.tonic.name == 'D'):
                    Leading_Num = Leading_Tone(note_list, SolFa_List)
                    CounterMelody_List.append(Leading_Num)
                else:
                    if needed_num == 0:  #
                        CounterMelody_List.append(Note_3rd)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 1:
                        CounterMelody_List.append(Note_5th)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 2:
                        CounterMelody_List.append(Note_6th)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 3:
                        CounterMelody_List.append(Note_8ve)
                        prev_c_num = CounterMelody_List[i - 1]

            if needed_num == 0 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:  # Normal cases
                CounterMelody_List.append(Note_3rd)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 1 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_5th)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 2 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_6th)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 3 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_8ve)
                prev_c_num = CounterMelody_List[i - 1]

        if Note_SolFaNameList3rd[7][i] == 7:
            Note_3rd = Note_SolFaNameList3rd[6].pop(0)
            Note_5th = Note_SolFaNameList5th[6].pop(0)
            Note_8ve = Note_SolFaNameList8ve[6].pop(0)
            Note_6th = Note_SolFaNameList6th[6].pop(0)
            print("intervals:")
            print(Note_3rd, Note_5th, Note_6th, Note_8ve)
            print("Previous_C_Num:")
            print(prev_c_num)
            L_note_3rd.append(Note_3rd)
            if i == len(Note_SolFaNameList3rd[7]) - 2 or i == len(Note_SolFaNameList3rd[7]) - 1:  # The last note
                CounterMelody_List.append(Note_8ve)
                FinalOrder_list5th.append(Note_5th)
                continue

            diff_check.append(Note_3rd - prev_c_num)
            diff_check.append(Note_5th - prev_c_num)
            diff_check.append(Note_6th - prev_c_num)
            diff_check.append(Note_8ve - prev_c_num)
            print(diff_check)

            if i > 1:
                # print("Flag")
                if cur_note_num > prev_note_num:  # ascending, need -ve notes for counter
                    print("Currently ascending!")
                    if min(diff_check) < 0:
                        if any(-3 <= elem < 0 for elem in diff_check):
                            needed_num = diff_check.index(max([no for no in diff_check if no < 0]))
                        else:
                            needed_num = diff_check.index(max([no for no in diff_check if no <= 0]))
                        # print("Flag")
                    else:
                        Note_8ve -= 12
                        Note_6th -= 12
                        Note_5th -= 12
                        Note_3rd -= 12
                        diff_check[0] = (int(Note_3rd - prev_c_num))
                        diff_check[1] = (int(Note_5th - prev_c_num))
                        diff_check[2] = (int(Note_6th - prev_c_num))
                        diff_check[3] = (int(Note_8ve - prev_c_num))
                        print(diff_check)
                        if any(-3 <= elem < 0 for elem in diff_check):
                            needed_num = diff_check.index(max([no for no in diff_check if no < 0]))
                        else:
                            needed_num = diff_check.index(max([no for no in diff_check if no <= 0]))
                else:  # descending, need +ve notes for counter
                    print("Currently descending!")
                    if max(diff_check) >= 0:
                        if any(3 >= elem > 0 for elem in diff_check):
                            needed_num = diff_check.index(min([no for no in diff_check if no > 0]))
                        else:
                            needed_num = diff_check.index(min([no for no in diff_check if no >= 0]))
                        # print("Flag")
                    else:
                        Note_8ve += 12
                        Note_6th += 12
                        Note_5th += 12
                        Note_3rd += 12
                        diff_check[0] = (int(Note_3rd - prev_c_num))
                        diff_check[1] = (int(Note_5th - prev_c_num))
                        diff_check[2] = (int(Note_6th - prev_c_num))
                        diff_check[3] = (int(Note_8ve - prev_c_num))
                        print(diff_check)
                        if any(3 >= elem > 0 for elem in diff_check):
                            needed_num = diff_check.index(min([no for no in diff_check if no > 0]))
                        else:
                            needed_num = diff_check.index(min([no for no in diff_check if no >= 0]))
                        # print("Flag")
                print("needed_num: ", needed_num)

            FinalOrder_list5th.append(Note_5th)
            if i == 0 or i == 1:
                prev_c_num = Note_8ve
                CounterMelody_List.append(Note_8ve)
            if i == len(Note_SolFaNameList3rd[7]) - 4 or i == len(Note_SolFaNameList3rd[7]) - 3:
                if melody_key.mode == 'major' and \
                        (melody_key.tonic.name == 'G' or melody_key.tonic.name == 'A' or melody_key.tonic.name == 'D'):
                    Leading_Num = Leading_Tone(note_list, SolFa_List)
                    CounterMelody_List.append(Leading_Num)
                else:
                    if needed_num == 0:
                        CounterMelody_List.append(Note_3rd)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 1:
                        CounterMelody_List.append(Note_5th)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 2:
                        CounterMelody_List.append(Note_6th)
                        prev_c_num = CounterMelody_List[i - 1]
                    if needed_num == 3:
                        CounterMelody_List.append(Note_8ve)
                        prev_c_num = CounterMelody_List[i - 1]

            if needed_num == 0 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:  # Normal cases
                CounterMelody_List.append(Note_3rd)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 1 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_5th)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 2 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_6th)
                prev_c_num = CounterMelody_List[i - 1]
            if needed_num == 3 and 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
                CounterMelody_List.append(Note_8ve)
                prev_c_num = CounterMelody_List[i - 1]

        diff_check = []  # reset list
        # 
        # if 1 < i < len(Note_SolFaNameList3rd[7]) - 4:
        #     input_current_SolFa_name = \
        #         Current_SolFa_Name(input_melody_key=melody_key.tonic.name, key_mode=melody_key.mode,
        #                            note_num=cur_note_num)
        #     counter_current_SolFa_name = \
        #         Current_SolFa_Name(input_melody_key=melody_key.tonic.name, key_mode=melody_key.mode,
        #                            note_num=CounterMelody_List[i])
        #     print("input:", input_current_SolFa_name)
        #     print("output:", counter_current_SolFa_name)
        #     differ = input_current_SolFa_name - counter_current_SolFa_name
        #     print("differ:", differ)
        #     if differ == 0:
        #         R = random.randint(0, 1)
        #         if R == 1:
        #             if counter_current_SolFa_name == 1 or counter_current_SolFa_name == 2 or \
        #                     counter_current_SolFa_name == 4 or counter_current_SolFa_name == 5:
        #                 CounterMelody_List[i] = CounterMelody_List[i] - 3
        #             else:
        #                 CounterMelody_List[i] = CounterMelody_List[i] - 4
        # debugging below
        print("CounterMelody_append_Num: ")
        print(CounterMelody_List[i])
        print("Current note num: ")
        print(cur_note_num)
        print("Previous note num: ")
        print(prev_note_num)
        if i % 2 == 1:
            prev_note_num = cur_note_num  # update previous note number to current note number
        # print("Program ran for the ", i+1, "th time")

    # -----------------Create the Tenor part which is the third track with long notes--------------------
    long_snd = []  # get 1st note of each bar
    long_snd_t = []  # get time of long sound list
    long_snd_fin = []  # doubles all elements within list
    long_snd_v = []  # self made velocity
    l_check = 4  # need to be checked for 1st time
    print("Generating Tenor......")
    print(Note_SolFaNameList3rd)
    print(note_list)
    print(time_list[0])
    for x in range(len(note_list[0])):  # G major test supposed results: 67,69,67,67,69,67,76,76,74,67
        if l_check == 4 and time_list[0][x + 1] != 1823:
            long_snd.append(L_note_3rd[x])
            l_check = 0
            print(x)
            continue
        else:
            if time_list[0][x] == 1823:  # whole note
                long_snd.append(L_note_3rd[x])
                print(x)
            elif time_list[0][x] == 911:  # half note
                l_check = l_check + 2
            elif time_list[0][x] == 455:  # quarter note
                l_check = l_check + 1
    print("Long sound list: ", long_snd)  # debug
    for y in range(len(long_snd)):
        if y == 0:  # pure hard-coding
            long_snd_t.append(0)
            long_snd_fin.append(long_snd[0] - 12)
            long_snd_t.append(1823)
            long_snd_fin.append(long_snd[0] - 12)
        else:
            long_snd_t.append(97)
            long_snd_fin.append(long_snd[y] - 12)
            long_snd_t.append(1823)
            long_snd_fin.append(long_snd[y] - 12)
        long_snd_v.append(80)
        long_snd_v.append(0)
    # LONG NOTES / Tenor PART ENDS HERE!

    # ------------------------------------Checking and Debug--------------------------------------
    print("long_snd_fin:", long_snd_fin)
    print("long_snd_t:", long_snd_t)
    print("long_snd_v:", long_snd_v)
    print("long_snd:", long_snd)
    print("L_note_3rd:", L_note_3rd)
    print("N_List: ", note_list[0])
    print("V_List: ", velocity_list[0])
    print("T_List: ", time_list[0])
    print("Counter_List: ", CounterMelody_List)
    print("Long sound list: ", long_snd_fin)
    print("Long sound v_list: ", long_snd_v)
    print("Long sound t_list: ", long_snd_t)
    print("MIDI data: ", mid)
    print("Mid_Track_Length: ", len(mid.tracks))
    print("List_Length: ", len(note_list[0]))
    print("List_Length: ", len(velocity_list[0]))
    print("List_Length: ", len(time_list[0]))
    print("Counter_List_Length:", len(CounterMelody_List))
    print("Long sound list length: ", len(long_snd_fin))
    # --------------------------------Put the note number Back to original midi file------------------------------------
    track1 = MidiTrack()
    track3rd = MidiTrack()
    long_note_track = MidiTrack()
    New_mid = MidiFile()
    print("Type_Of_Track: ", type(track3rd))
    New_mid.tracks.append(track1)
    New_mid.tracks.append(track3rd)
    New_mid.tracks.append(long_note_track)
    track1.append(Message('program_change', channel=0, program=40, time=0))
    track1.append(MetaMessage('set_tempo', tempo=Tempo, time=0))
    for j in range(len(channel_list[0])):
        track1.append(Message('note_on', note=note_list[0][j], velocity=velocity_list[0][j], time=time_list[0][j]))

    track3rd.append(Message('program_change', channel=0, program=41, time=0))
    track3rd.append(MetaMessage('set_tempo', tempo=Tempo, time=0))
    for j in range(len(CounterMelody_List)):
        track3rd.append(
            Message('note_on', note=CounterMelody_List[j], velocity=velocity_list[0][j], time=time_list[0][j]))

    long_note_track.append(Message('program_change', channel=0, program=42, time=0))
    long_note_track.append(MetaMessage('set_tempo', tempo=Tempo, time=0))
    for j in range(len(long_snd_fin)):
        long_note_track.append(
            Message('note_on', note=long_snd_fin[j], velocity=long_snd_v[j], time=long_snd_t[j]))
    New_mid.save('./music/Output/Type1/new_song3rd.mid')
    if system_name == "Windows":
        try:
            f = win32api.ShellExecute(0, 'open', 'MuseScore3.exe', './music/Output/Type1/new_song3rd.mid', '', 1)
        except BaseException:
            MuseScore = 0
            # Debug
            print(MuseScore)
            print("打开乐谱失败")
        else:
            print(f)
            if f == 42:
                MuseScore = 1
                print("打开乐谱成功")
            else:
                MuseScore = 0
                print("打开乐谱失敗")
        finally:
            print("try 結束")

    elif system_name == "Darwin":
        try:
            f = os.system("open -a MuseScore\ 3 ./music/Output/Type1/new_song3rd.mid")
        except BaseException:
            MuseScore = 0
            # Debug
            print(MuseScore)
            print("打开乐谱失败")
        else:
            print("f:", f)
            if f == 0:
                MuseScore = 1
                print("打开乐谱成功")
            else:
                MuseScore = 0
                print("打开乐谱失敗")
        finally:
            print("try 結束")
    else:
        print("Please use this Application in Windows or Darwin/Mac system to have a better use.")
    New3rd = converter.parse('./music/Output/Type1/new_song3rd.mid')
    New3rd.write("xml", "./music/Output/Type1/new_song3rd.xml")
    # ---------------------------------------------------second MIDI file for base chords-----------------------------
    New_mid5th = MidiFile()
    track1_1 = MidiTrack()
    track3_3rd = MidiTrack()
    track5th = MidiTrack()
    New_mid5th.tracks.append(track1_1)
    track1_1.append(Message('program_change', channel=2, program=0, time=0))
    for j in range(len(channel_list[0])):
        track1_1.append(Message('note_on', note=note_list[0][j], velocity=velocity_list[0][j], time=time_list[0][j]))

    New_mid5th.tracks.append(track3_3rd)
    track3_3rd.append(Message('program_change', channel=2, program=0, time=0))
    for j in range(len(CounterMelody_List)):
        track3_3rd.append(
            Message('note_on', note=CounterMelody_List[j], velocity=velocity_list[0][j], time=time_list[0][j]))

    New_mid5th.tracks.append(track5th)
    track5th.append(Message('program_change', channel=2, program=42, time=0))
    for j in range(len(FinalOrder_list5th)):
        track5th.append(Message('note_on', channel=15, note=FinalOrder_list5th[j], velocity=velocity_list[0][j],
                                time=time_list[0][j]))

    New_mid5th.save('./music/Output/Type1/new_song5th.mid')
    New5th = converter.parse('./music/Output/Type1/new_song5th.mid')
    New5th.write("xml", "./music/Output/Type1/new_song5th.xml")
    s = converter.parse('./music/Output/Type1/new_song5th.mid')
    sChords = s.chordify()
    print("sChords_Info: ", sChords)

    sFlat = sChords.flat
    print("sFlat_Info: ", sFlat)

    sOnlyChords = sFlat.getElementsByClass('Chord')
    print("sOnlyChords_Info: ", sOnlyChords)

    displayPart = stream.Part(id='displayPart')
    print("displayPart_Info: ", displayPart)

    def appendChordPairs(this_Chord, next_Chord):
        # if (thisChord.isTriad() is True or
        #         thisChord.isSeventh() is True and
        #         thisChord.root().name == 'F'):
        closePositionThisChord = this_Chord.closedPosition(forceOctave=4)
        closePositionNextChord = next_Chord.closedPosition(forceOctave=4)

        m = stream.Measure()
        m.append(closePositionThisChord)
        m.append(closePositionNextChord)
        displayPart.append(m)

    for i in range(len(sOnlyChords) - 1):
        thisChord = sOnlyChords[i]
        nextChord = sOnlyChords[i + 1]
        appendChordPairs(thisChord, nextChord)

    print("display_part_Length: ", len(displayPart))

    print(melody_key.tonic.name, melody_key.mode)
    for c in displayPart.recurse().getElementsByClass('Chord'):
        rn = roman.romanNumeralFromChord(c, melody_key)
        c.addLyric(str(rn.figure))
    for c in sChords.recurse().getElementsByClass('Chord'):
        rn = roman.romanNumeralFromChord(c, melody_key)
        c.closedPosition(forceOctave=4)
        c.addLyric(str(rn.figure))
    #

    # displayPart.plot('piano-roll')
    # s.plot('piano-roll')
    # sChords.plot('piano-roll')
    # displayPart.show()
    # sChords.show()
    sChords.write("midi", "./music/Output/Type1/sChords.mid")
    sChords.write("xml", "./music/Output/Type1/sChords.xml")
    fp1 = os.path.join('./music/Output/Type1', "new_song3rd.mid")
    fp2 = os.path.join('./music/Output/Type1', "sChords.mid")
    Add_Base_Chords_type1(fp1, fp2)
    # ---------------------------------------------Type2 Chords----------------------------------------------
    New_mid = MidiFile()
    track3_3rd = MidiTrack()
    track5th = MidiTrack()
    New_mid.tracks.append(track3_3rd)
    track3_3rd.append(Message('program_change', channel=2, program=0, time=0))
    # for j in range(len(CounterMelody_List)):
    #    track3_3rd.append(
    #        Message('note_on', note=CounterMelody_List[j], velocity=velocity_list[0][j], time=time_list[0][j]))
    for j in range(len(long_snd_fin)):
        track3_3rd.append(
            Message('note_on', note=long_snd_fin[j], velocity=long_snd_v[j], time=long_snd_t[j]))
        # track3_3rd.append(
        #    Message('note_on', note=long_snd_fin[j], velocity=long_snd_v[j], time=long_snd_t[j]))

    New_mid.tracks.append(track5th)
    track5th.append(Message('program_change', channel=2, program=0, time=0))
    for j in range(len(FinalOrder_list5th)):
        track5th.append(Message('note_on', channel=15, note=FinalOrder_list5th[j], velocity=velocity_list[0][j],
                                time=time_list[0][j]))

    New_mid.save('./music/Output/Type2/new_song3+5.mid')
    New = converter.parse('./music/Output/Type2/new_song3+5.mid')
    New.write("xml", "./music/Output/Type2/new_song3+5.xml")
    s1 = converter.parse('./music/Output/Type2/new_song3+5.xml')

    sChords = s1.chordify()
    print("sChords_Info: ", sChords)

    sFlat = sChords.flat
    print("sFlat_Info: ", sFlat)

    sOnlyChords = sFlat.getElementsByClass('Chord')
    print("sOnlyChords_Info: ", sOnlyChords)

    displayPart = stream.Part(id='displayPart')
    print("display_Part_Info: ", displayPart)

    def appendChordPairs(this_Chord, next_Chord):
        # if (thisChord.isTriad() is True or
        #         thisChord.isSeventh() is True and
        #         thisChord.root().name == 'F'):
        closePositionThisChord = this_Chord.closedPosition(forceOctave=4)
        closePositionNextChord = next_Chord.closedPosition(forceOctave=4)

        m = stream.Measure()
        m.append(closePositionThisChord)
        m.append(closePositionNextChord)
        displayPart.append(m)

    for i in range(len(sOnlyChords) - 1):
        thisChord = sOnlyChords[i]
        nextChord = sOnlyChords[i + 1]
        appendChordPairs(thisChord, nextChord)

    print("display_part_Length: ", len(displayPart))

    print(melody_key.tonic.name, melody_key.mode)
    for c in displayPart.recurse().getElementsByClass('Chord'):
        rn = roman.romanNumeralFromChord(c, melody_key)
        c.addLyric(str(rn.figure))
    for c in sChords.recurse().getElementsByClass('Chord'):
        rn = roman.romanNumeralFromChord(c, melody_key)
        c.closedPosition(forceOctave=4)
        c.addLyric(str(rn.figure))

    sChords.write("midi", "./music/Output/Type2/sChords.mid")
    sChords.write("xml", "./music/Output/Type2/sChords.xml")
    fp3 = os.path.join('./music/Output/Type1', "new_song3rd.mid")
    fp4 = os.path.join('./music/Output/Type2', "sChords.mid")
    Add_Base_Chords_type2(fp3, fp4)
    # ------------------------------Type3______________--------------------------------------------------
    New_mid = MidiFile()
    track1_1 = MidiTrack()
    track3_3rd = MidiTrack()
    track5th = MidiTrack()
    New_mid.tracks.append(track1_1)
    track1_1.append(Message('program_change', channel=2, program=40, time=0))
    for j in range(len(channel_list[0])):
        track1_1.append(Message('note_on', note=note_list[0][j], velocity=velocity_list[0][j], time=time_list[0][j]))

    New_mid.tracks.append(track3_3rd)
    track3_3rd.append(Message('program_change', channel=2, program=41, time=0))
    # for j in range(len(CounterMelody_List)):
    #    track3_3rd.append(
    #        Message('note_on', note=CounterMelody_List[j], velocity=velocity_list[0][j], time=time_list[0][j]))
    for j in range(len(long_snd_fin)):
        track3_3rd.append(
            Message('note_on', note=long_snd_fin[j], velocity=long_snd_v[j], time=long_snd_t[j]))

    New_mid.tracks.append(track5th)
    track5th.append(Message('program_change', channel=2, program=70, time=0))
    for j in range(len(FinalOrder_list5th)):
        track5th.append(Message('note_on', channel=15, note=FinalOrder_list5th[j], velocity=velocity_list[0][j],
                                time=time_list[0][j]))

    New_mid.save('./music/Output/Type3/New_Song_Type3.mid')
    New = converter.parse('./music/Output/Type3/New_Song_Type3.mid')
    New.write("xml", "./music/Output/Type3/New_Song_Type3.xml")
    New.write("midi", "./music/Output/Type3/New_Song_Type3.mid")
    s2 = converter.parse('./music/Output/Type3/New_Song_Type3.xml')
    sChords = s2.chordify()

    print("sChords_Info: ", sChords)

    sFlat = sChords.flat
    print("sFlat_Info: ", sFlat)

    sOnlyChords = sFlat.getElementsByClass('Chord')
    print("sOnlyChords_Info: ", sOnlyChords)

    displayPart = stream.Part(id='displayPart')
    print("display_Part_Info: ", displayPart)

    def appendChordPairs(this_Chord, next_Chord):
        # if (thisChord.isTriad() is True or
        #         thisChord.isSeventh() is True and
        #         thisChord.root().name == 'F'):
        closePositionThisChord = this_Chord.closedPosition(forceOctave=4)
        closePositionNextChord = next_Chord.closedPosition(forceOctave=4)

        m = stream.Measure()
        m.append(closePositionThisChord)
        m.append(closePositionNextChord)
        displayPart.append(m)

    for i in range(len(sOnlyChords) - 1):
        thisChord = sOnlyChords[i]
        nextChord = sOnlyChords[i + 1]
        appendChordPairs(thisChord, nextChord)

    print("display_part_Length: ", len(displayPart))

    print(melody_key.tonic.name, melody_key.mode)
    for c in displayPart.recurse().getElementsByClass('Chord'):
        rn = roman.romanNumeralFromChord(c, melody_key)
        c.addLyric(str(rn.figure))
    for c in sChords.recurse().getElementsByClass('Chord'):
        rn = roman.romanNumeralFromChord(c, melody_key)
        c.closedPosition(forceOctave=4)
        c.addLyric(str(rn.figure))

    sChords.write("midi", "./music/Output/Type3/sChords.mid")
    sChords.write("xml", "./music/Output/Type3/sChords.xml")

    return MuseScore
# if __name__ == '__main__':
#     melody_generate()
