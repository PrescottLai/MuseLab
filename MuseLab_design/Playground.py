import numpy as np
from Add_BaseChord import *
from Functions import *
from mido import MetaMessage


def Own_Creation(file_path, instrument_List):
    print(file_path)
    print(instrument_List)
    s = converter.parse(file_path)
    mid = MidiFile(file_path)
    Input_File = "Input.mid"
    Input_File_name = check_filename_available(Input_File)
    s.write("midi", "./music/Output/" + Input_File_name)
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
    L_note_5th = []
    print("Generating Alto/Counter Melody......")
    for i in range(len(Note_SolFaNameList3rd[7])):
        # debug
        print("i_Number: ", i)
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
            L_note_5th.append(Note_5th)
            if i == len(Note_SolFaNameList3rd[7]) - 2 or i == len(Note_SolFaNameList3rd[7]) - 1:  # The last note
                CounterMelody_List.append(Note_8ve)
                FinalOrder_list5th.append(Note_5th)
                if i % 2 == 1:
                    if CounterMelody_List[i] - CounterMelody_List[i - 2] > 10:
                        CounterMelody_List[i] = CounterMelody_List[i] - 12
                        CounterMelody_List[i - 1] = CounterMelody_List[i]
                        prev_c_num = CounterMelody_List[i]
                    elif CounterMelody_List[i] - CounterMelody_List[i - 2] < -10:
                        CounterMelody_List[i] = CounterMelody_List[i] + 12
                        CounterMelody_List[i - 1] = CounterMelody_List[i]
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
            L_note_5th.append(Note_5th)
            if i == len(Note_SolFaNameList3rd[7]) - 2 or i == len(Note_SolFaNameList3rd[7]) - 1:  # The last note
                CounterMelody_List.append(Note_8ve)
                FinalOrder_list5th.append(Note_5th)
                if i % 2 == 1:
                    if CounterMelody_List[i] - CounterMelody_List[i - 2] > 10:
                        CounterMelody_List[i] = CounterMelody_List[i] - 12
                        CounterMelody_List[i - 1] = CounterMelody_List[i]
                        prev_c_num = CounterMelody_List[i]
                    elif CounterMelody_List[i] - CounterMelody_List[i - 2] < -10:
                        CounterMelody_List[i] = CounterMelody_List[i] + 12
                        CounterMelody_List[i - 1] = CounterMelody_List[i]
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
            L_note_5th.append(Note_5th)
            if i == len(Note_SolFaNameList3rd[7]) - 2 or i == len(Note_SolFaNameList3rd[7]) - 1:  # The last note
                CounterMelody_List.append(Note_8ve)
                FinalOrder_list5th.append(Note_5th)
                if i % 2 == 1:
                    if CounterMelody_List[i] - CounterMelody_List[i - 2] > 10:
                        CounterMelody_List[i] = CounterMelody_List[i] - 12
                        CounterMelody_List[i - 1] = CounterMelody_List[i]
                        prev_c_num = CounterMelody_List[i]
                    elif CounterMelody_List[i] - CounterMelody_List[i - 2] < -10:
                        CounterMelody_List[i] = CounterMelody_List[i] + 12
                        CounterMelody_List[i - 1] = CounterMelody_List[i]
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
            L_note_5th.append(Note_5th)
            if i == len(Note_SolFaNameList3rd[7]) - 2 or i == len(Note_SolFaNameList3rd[7]) - 1:  # The last note
                if i % 2 == 1:
                    if CounterMelody_List[i] - CounterMelody_List[i - 2] > 10:
                        CounterMelody_List[i] = CounterMelody_List[i] - 12
                        CounterMelody_List[i - 1] = CounterMelody_List[i]
                        prev_c_num = CounterMelody_List[i]
                    elif CounterMelody_List[i] - CounterMelody_List[i - 2] < -10:
                        CounterMelody_List[i] = CounterMelody_List[i] + 12
                        CounterMelody_List[i - 1] = CounterMelody_List[i]
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
            L_note_5th.append(Note_5th)
            if i == len(Note_SolFaNameList3rd[7]) - 2 or i == len(Note_SolFaNameList3rd[7]) - 1:  # The last note
                CounterMelody_List.append(Note_8ve)
                FinalOrder_list5th.append(Note_5th)
                if i % 2 == 1:
                    if CounterMelody_List[i] - CounterMelody_List[i - 2] > 10:
                        CounterMelody_List[i] = CounterMelody_List[i] - 12
                        CounterMelody_List[i - 1] = CounterMelody_List[i]
                        prev_c_num = CounterMelody_List[i]
                    elif CounterMelody_List[i] - CounterMelody_List[i - 2] < -10:
                        CounterMelody_List[i] = CounterMelody_List[i] + 12
                        CounterMelody_List[i - 1] = CounterMelody_List[i]
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
            L_note_5th.append(Note_5th)
            if i == len(Note_SolFaNameList3rd[7]) - 2 or i == len(Note_SolFaNameList3rd[7]) - 1:  # The last note
                CounterMelody_List.append(Note_8ve)
                FinalOrder_list5th.append(Note_5th)
                if i % 2 == 1:
                    if CounterMelody_List[i] - CounterMelody_List[i - 2] > 10:
                        CounterMelody_List[i] = CounterMelody_List[i] - 12
                        CounterMelody_List[i - 1] = CounterMelody_List[i]
                        prev_c_num = CounterMelody_List[i]
                    elif CounterMelody_List[i] - CounterMelody_List[i - 2] < -10:
                        CounterMelody_List[i] = CounterMelody_List[i] + 12
                        CounterMelody_List[i - 1] = CounterMelody_List[i]
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
                        while Note_8ve - prev_c_num < 0:
                            Note_8ve += 12
                        while Note_6th - prev_c_num < 0:
                            Note_6th += 12
                        while Note_5th - prev_c_num < 0:
                            Note_5th += 12
                        while Note_3rd - prev_c_num < 0:
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
            L_note_5th.append(Note_5th)
            if i == len(Note_SolFaNameList3rd[7]) - 2 or i == len(Note_SolFaNameList3rd[7]) - 1:  # The last note
                CounterMelody_List.append(Note_8ve)
                FinalOrder_list5th.append(Note_5th)
                if i % 2 == 1:
                    if CounterMelody_List[i] - CounterMelody_List[i - 2] > 10:
                        CounterMelody_List[i] = CounterMelody_List[i] - 12
                        CounterMelody_List[i - 1] = CounterMelody_List[i]
                        prev_c_num = CounterMelody_List[i]
                    elif CounterMelody_List[i] - CounterMelody_List[i - 2] < -10:
                        CounterMelody_List[i] = CounterMelody_List[i] + 12
                        CounterMelody_List[i - 1] = CounterMelody_List[i]
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
        if (1 < i < len(Note_SolFaNameList3rd[7]) - 4) and (i % 2 == 1):
            input_current_SolFa_name = \
                Current_SolFa_Name(input_melody_key=melody_key.tonic.name, key_mode=melody_key.mode,
                                   note_num=cur_note_num)
            counter_current_SolFa_name = \
                Current_SolFa_Name(input_melody_key=melody_key.tonic.name, key_mode=melody_key.mode,
                                   note_num=CounterMelody_List[i])
            print("input:", input_current_SolFa_name)
            print("output:", counter_current_SolFa_name)
            differ = input_current_SolFa_name - counter_current_SolFa_name
            print("differ:", differ)
            # 尽量避免太多Unison的重复。
            if differ == 0:
                R = np.random.choice([0, 1, 2], replace=True, p=[0.4, 0.4, 0.2])
                # R = random.randint(0, 1)
                print("Random Number:", R)
                print("CounterMelody_append_Num: ")
                print(CounterMelody_List[i])
                if R == 0:
                    if counter_current_SolFa_name == 1 or counter_current_SolFa_name == 2 or \
                            counter_current_SolFa_name == 4 or counter_current_SolFa_name == 5:
                        CounterMelody_List[i - 1] = CounterMelody_List[i - 1] - 3
                        CounterMelody_List[i] = CounterMelody_List[i] - 3
                        prev_c_num = CounterMelody_List[i]
                    else:
                        CounterMelody_List[i - 1] = CounterMelody_List[i - 1] - 4
                        CounterMelody_List[i] = CounterMelody_List[i] - 4
                        prev_c_num = CounterMelody_List[i]
                elif R == 1:
                    if counter_current_SolFa_name == 1 or counter_current_SolFa_name == 4 \
                            or counter_current_SolFa_name == 5:
                        CounterMelody_List[i - 1] = CounterMelody_List[i - 1] + 4
                        CounterMelody_List[i] = CounterMelody_List[i] + 4
                        prev_c_num = CounterMelody_List[i]
                    else:
                        CounterMelody_List[i - 1] = CounterMelody_List[i - 1] + 3
                        CounterMelody_List[i] = CounterMelody_List[i] + 3
                        prev_c_num = CounterMelody_List[i]

            # 避免Counter Melody 音与音直接跨度太大而导致旋律不连贯, 避免过多的重复音出现在Counter Melody
        if i > 1 and i % 2 == 1:
            if CounterMelody_List[i] - CounterMelody_List[i - 2] > 12:
                CounterMelody_List[i] = CounterMelody_List[i] - 12
                CounterMelody_List[i - 1] = CounterMelody_List[i]
                prev_c_num = CounterMelody_List[i]
            elif CounterMelody_List[i] - CounterMelody_List[i - 2] < -12:
                CounterMelody_List[i] = CounterMelody_List[i] + 12
                CounterMelody_List[i - 1] = CounterMelody_List[i]
                prev_c_num = CounterMelody_List[i]
            elif CounterMelody_List[i] - CounterMelody_List[i - 2] == 0:
                counter_current_SolFa_name = \
                    Current_SolFa_Name(input_melody_key=melody_key.tonic.name, key_mode=melody_key.mode,
                                       note_num=CounterMelody_List[i])
                R = np.random.choice([0, 1], replace=True, p=[0.5, 0.5])
                if R == 1:
                    if counter_current_SolFa_name == 1 or counter_current_SolFa_name == 4 \
                            or counter_current_SolFa_name == 5:
                        CounterMelody_List[i - 1] = CounterMelody_List[i - 1] + 4
                        CounterMelody_List[i] = CounterMelody_List[i] + 4
                        prev_c_num = CounterMelody_List[i]
                    else:
                        CounterMelody_List[i - 1] = CounterMelody_List[i - 1] + 3
                        CounterMelody_List[i] = CounterMelody_List[i] + 3
                        prev_c_num = CounterMelody_List[i]

        # debugging below
        print("CounterMelody_append_Num_after: ")
        print(CounterMelody_List[i])
        print("Current note num: ")
        print(cur_note_num)
        print("Previous note num: ")
        print(prev_note_num)
        if i % 2 == 1:
            prev_note_num = cur_note_num  # update previous note number to current note number
        # print("Program ran for the ", i+1, "th time")

    # -----------------Create the Tenor part which is the third track with long notes in 4/4 Rhythm--------------------
    # We can get the numerator and denominator in MIDI file and set the different rules.
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
        if l_check >= 4 and time_list[0][x + 1] != 1823:
            if l_check > 4 and x != 0:
                long_snd.append(L_note_3rd[x - 1])
                l_check = l_check - 4
            else:
                long_snd.append(L_note_3rd[x])
                l_check = l_check - 4
            print("这是什么：", x)
            # continue
        else:
            if time_list[0][x] == 1823:  # whole note
                long_snd.append(L_note_3rd[x])
                print(x)
            elif time_list[0][x] == 911:  # half note
                l_check = l_check + 2
            elif time_list[0][x] == 455:  # quarter note
                l_check = l_check + 1
            elif time_list[0][x] == 227:
                l_check = l_check + 0.5
            elif time_list[0][x] == 1139:
                l_check = l_check + 1.5
            elif time_list[0][x] == 1367:
                l_check = l_check + 3
            elif time_list[0][x] == 2279:
                l_check = l_check + 5
    if l_check > 4:
        long_snd.append(L_note_3rd[:-1])
        l_check = l_check - 4
    print("Long sound list: ", long_snd)  # debug
    print("l_check: ", l_check)

    for y in range(len(long_snd)):
        if y == 0:  # pure hard-coding
            long_snd_t.append(0)
            long_snd_fin.append(long_snd[0] - 24)
            long_snd_t.append(1823)
            long_snd_fin.append(long_snd[0] - 24)
        elif y == len(long_snd) - 1:
            long_snd_t.append(97)
            long_snd_fin.append(long_snd[0] - 24)
            if l_check == 0.5:
                long_snd_t.append(227)
                long_snd_fin.append(long_snd[0] - 24)
            elif l_check == 1:
                long_snd_t.append(455)
                long_snd_fin.append(long_snd[0] - 24)
            elif l_check == 1.5:
                long_snd_t.append(1139)
                long_snd_fin.append(long_snd[0] - 24)
            elif l_check == 2:
                long_snd_t.append(911)
                long_snd_fin.append(long_snd[0] - 24)

            # NOTE TO SELF:
            # NEEDS TO ADD l_check == 2.5 and l_check == 3.5 CASES HERE!!!
            # CURRENTLY MISSING!!

            elif l_check == 3:
                long_snd_t.append(1367)
                long_snd_fin.append(long_snd[0] - 24)
            elif l_check == 4:
                long_snd_t.append(1823)
                long_snd_fin.append(long_snd[0] - 24)
        else:
            long_snd_t.append(97)
            long_snd_fin.append(long_snd[y] - 24)
            long_snd_t.append(1823)
            long_snd_fin.append(long_snd[y] - 24)
        long_snd_v.append(80)
        long_snd_v.append(0)
    # LONG NOTES / Tenor PART ENDS HERE!

    # long_snd_5 = []  # get 1st note of each bar
    # long_snd_t_5 = []  # get time of long sound list
    # long_snd_fin_5 = []  # doubles all elements within list
    # long_snd_v_5 = []  # self made velocity
    # l_check = 4  # need to be checked for 1st time
    # print("Generating Tenor......")
    # print(Note_SolFaNameList3rd)
    # print(note_list)
    # print(time_list[0])
    # for x in range(len(note_list[0])):  # G major test supposed results: 67,69,67,67,69,67,76,76,74,67
    #     if l_check >= 4 and time_list[0][x + 1] != 1823:
    #         if l_check > 4 and x != 0:
    #             long_snd_5.append(L_note_5th[x - 1])
    #             l_check = l_check - 4
    #         else:
    #             long_snd_5.append(L_note_5th[x])
    #             l_check = l_check - 4
    #         print("这是什么：", x)
    #         # continue
    #     else:
    #         if time_list[0][x] == 1823:  # whole note
    #             long_snd_5.append(L_note_5th[x])
    #             print(x)
    #         elif time_list[0][x] == 911:  # half note
    #             l_check = l_check + 2
    #         elif time_list[0][x] == 455:  # quarter note
    #             l_check = l_check + 1
    #         elif time_list[0][x] == 227:
    #             l_check = l_check + 0.5
    #         elif time_list[0][x] == 1139:
    #             l_check = l_check + 1.5
    #         elif time_list[0][x] == 1367:
    #             l_check = l_check + 3
    #         elif time_list[0][x] == 2279:
    #             l_check = l_check + 5
    # if l_check > 4:
    #     long_snd_5.append(L_note_5th[:-1])
    #     l_check = l_check - 4
    # print("Long sound list_5: ", long_snd_5)  # debug
    # print("l_check: ", l_check)
    #
    # for y in range(len(long_snd_5)):
    #     if y == 0:  # pure hard-coding
    #         long_snd_t_5.append(0)
    #         long_snd_fin_5.append(long_snd_5[0] - 12)
    #         long_snd_t_5.append(1823)
    #         long_snd_fin_5.append(long_snd_5[0] - 12)
    #     elif y == len(long_snd_5) - 1:
    #         long_snd_t_5.append(97)
    #         long_snd_fin_5.append(long_snd_5[0] - 12)
    #         if l_check == 0.5:
    #             long_snd_t_5.append(227)
    #             long_snd_fin_5.append(long_snd_5[0] - 12)
    #         elif l_check == 1:
    #             long_snd_t_5.append(455)
    #             long_snd_fin_5.append(long_snd_5[0] - 12)
    #         elif l_check == 1.5:
    #             long_snd_t_5.append(1139)
    #             long_snd_fin_5.append(long_snd_5[0] - 12)
    #         elif l_check == 2:
    #             long_snd_t_5.append(911)
    #             long_snd_fin_5.append(long_snd_5[0] - 12)
    #
    #         # NOTE TO SELF:
    #         # NEEDS TO ADD l_check == 2.5 and l_check == 3.5 CASES HERE!!!
    #         # CURRENTLY MISSING!!
    #
    #         elif l_check == 3:
    #             long_snd_t_5.append(1367)
    #             long_snd_fin_5.append(long_snd_5[0] - 12)
    #         elif l_check == 4:
    #             long_snd_t_5.append(1823)
    #             long_snd_fin_5.append(long_snd_5[0] - 12)
    #     else:
    #         long_snd_t_5.append(97)
    #         long_snd_fin_5.append(long_snd_5[y] - 12)
    #         long_snd_t_5.append(1823)
    #         long_snd_fin_5.append(long_snd_5[y] - 12)
    #     long_snd_v_5.append(80)
    #     long_snd_v_5.append(0)
    # ------------------------------------Checking and Debug--------------------------------------
    print("long_snd_fin:", long_snd_fin)
    print("long_snd_t:", long_snd_t)
    print("long_snd_v:", long_snd_v)
    print("long_snd:", long_snd)
    print("L_note_3rd:", L_note_3rd)
    # print("long_snd_fin_5:", long_snd_fin_5)
    # print("long_snd_t_5:", long_snd_t_5)
    # print("long_snd_v_5:", long_snd_v_5)
    # print("long_snd_5:", long_snd_5)
    # print("L_note_5th:", L_note_5th)
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
    # --------------------------------Create a new Midi File------------------------------------
    track3_note = long_snd_fin
    # #if Rhythm quarter note ----
    track3_note_new = []
    track3_time = []
    track3_velocity = []
    if instrument_List[5] == 1:

        n = 1
        for i in range(len(track3_note)):
            if i < len(track3_note)-2:
                for j in range(4):
                    if i == 0 and j == 0 and n == 1:
                        track3_time.append(0)
                        track3_velocity.append(80)
                    if j % 2 == 0 and n == 0:
                        track3_velocity.append(80)
                        track3_time.append(25)
                    elif j % 2 == 1:
                        track3_time.append(455)
                        track3_velocity.append(0)
                    n = 0
                    track3_note_new.append(track3_note[i])
            else:
                if i % 2 == 0:
                    track3_time.append(25)
                    track3_velocity.append(80)
                else:
                    track3_velocity.append(0)
                    track3_time.append(long_snd_t[i])
                track3_note_new.append(track3_note[i])

    # # if Rhythm half note ----
    if instrument_List[5] == 2:

        n = 1
        for i in range(len(track3_note)):
            if i < len(track3_note)-2:
                for j in range(2):
                    if i == 0 and j == 0 and n == 1:
                        track3_time.append(0)
                        track3_velocity.append(80)
                    if j % 2 == 0 and n == 0:
                        track3_velocity.append(80)
                        track3_time.append(49)
                    elif j % 2 == 1:
                        track3_time.append(911)
                        track3_velocity.append(0)
                    n = 0
                    track3_note_new.append(track3_note[i])
            else:
                if i % 2 == 0:
                    track3_time.append(49)
                    track3_velocity.append(80)
                else:
                    track3_velocity.append(0)
                    track3_time.append(long_snd_t[i])
                track3_note_new.append(track3_note[i])

    # # if Rhythm quaver/eighth note
    if instrument_List[5] == 3:

        n = 1
        for i in range(len(track3_note)):
            if i < len(track3_note)-2:
                for j in range(8):
                    if i == 0 and j == 0 and n == 1:
                        track3_time.append(0)
                        track3_velocity.append(80)
                    if j % 2 == 0 and n == 0:
                        track3_velocity.append(80)
                        track3_time.append(13)
                    elif j % 2 == 1:
                        track3_time.append(227)
                        track3_velocity.append(0)
                    n = 0
                    track3_note_new.append(track3_note[i])
            else:
                if i % 2 == 0:
                    track3_time.append(13)
                    track3_velocity.append(80)
                else:
                    track3_velocity.append(0)
                    track3_time.append(long_snd_t[i])
                track3_note_new.append(track3_note[i])

    # # if Rhythm doted half note
    if instrument_List[5] == 4:
        for i in range(len(track3_note)):
            if i < len(track3_note)-2:
                if i % 2 == 0:
                    for j in range(4):
                        if i == 0 and j == 0:
                            track3_velocity.append(80)
                            track3_time.append(0)
                        elif j == 0:
                            track3_velocity.append(80)
                            track3_time.append(25)
                        elif j == 1:
                            track3_velocity.append(0)
                            track3_time.append(455)
                        elif j == 2:
                            track3_velocity.append(80)
                            track3_time.append(25)
                        elif j == 3:
                            track3_velocity.append(0)
                            track3_time.append(683)
                        track3_note_new.append(track3_note[i])
                elif i % 2 == 1:
                    for j in range(4):
                        if j == 0:
                            track3_velocity.append(80)
                            track3_time.append(37)
                        elif j == 1:
                            track3_velocity.append(0)
                            track3_time.append(227)
                        elif j == 2:
                            track3_velocity.append(80)
                            track3_time.append(13)
                        elif j == 3:
                            track3_velocity.append(0)
                            track3_time.append(455)
                        track3_note_new.append(track3_note[i])
            else:
                if i % 2 == 0:
                    track3_time.append(25)
                    track3_velocity.append(80)
                else:
                    track3_velocity.append(0)
                    track3_time.append(long_snd_t[i])
                track3_note_new.append(track3_note[i])
    print(track3_note)
    print(track3_note_new)
    print(track3_velocity)
    print(track3_time)
    print("track3_note_length: ", len(track3_note_new))
    print("track3_velocity_length: ", len(track3_velocity))
    print("track3_time_length: ", len(track3_time))
    print("Max and min of original note list: ", max(note_list[0]), " and ", min(note_list[0]))
    print("Max and min of counter melody: ", max(CounterMelody_List), " and ", min(CounterMelody_List))
    print("Max and min of track3_note: ", max(track3_note) + 12, " and ", min(track3_note) + 12)
    print("Max and min of long_snd_fin: ", max(long_snd_fin), " and ", min(long_snd_fin))


    # Each part total tracks number and create the MIDI track list
    Tracks = [len(instrument_List[1]), len(instrument_List[2]), len(instrument_List[3]), len(instrument_List[4])]
    part1, part2, part3, part4 = [], [], [], []
    for i in range(Tracks[0]):
        part1.append(MidiTrack())
    for i in range(Tracks[1]):
        part2.append(MidiTrack())
    for i in range(Tracks[2]):
        part3.append(MidiTrack())
    for i in range(Tracks[3]):
        part4.append(MidiTrack())

    New_mid = MidiFile()
    # Melody part
    for i in range(len(part1)):
        New_mid.tracks.append(part1[i])
        part1[i].append(Message('program_change', channel=0, program=instrument_List[1][i]-1, time=0))
        part1[i].append(MetaMessage('set_tempo', tempo=Tempo, time=0))
        for j in range(len(channel_list[0])):
            part1[i].append(Message('note_on', note=note_list[0][j], velocity=velocity_list[0][j], time=time_list[0][j]))

    # Counter Melody part
    for i in range(len(part2)):
        New_mid.tracks.append(part2[i])
        part2[i].append(Message('program_change', channel=0, program=instrument_List[2][i]-1, time=0))
        part2[i].append(MetaMessage('set_tempo', tempo=Tempo, time=0))
        for j in range(len(CounterMelody_List)):
            if j % 2 == 0:
                part2[i].append(
                    Message('note_on', note=CounterMelody_List[j], velocity=velocity_list[0][j] - 20, time=time_list[0][j]))
            else:
                part2[i].append(
                    Message('note_on', note=CounterMelody_List[j], velocity=velocity_list[0][j], time=time_list[0][j]))

    # Rhythm part
    for i in range(len(part3)):
        New_mid.tracks.append(part3[i])
        part3[i].append(Message('program_change', channel=0, program=instrument_List[3][i]-1, time=0))
        part3[i].append(MetaMessage('set_tempo', tempo=Tempo, time=0))
        for j in range(len(track3_note_new)):
            if j % 2 == 0:
                part3[i].append(
                    Message('note_on', note=track3_note_new[j] + 12, velocity=track3_velocity[j] - 20,
                            time=track3_time[j]))
            else:
                part3[i].append(
                    Message('note_on', note=track3_note_new[j] + 12, velocity=track3_velocity[j], time=track3_time[j]))

    # Base part
    for i in range(len(part4)):
        New_mid.tracks.append(part4[i])
        part4[i].append(Message('program_change', channel=0, program=instrument_List[4][i]-1, time=0))
        part4[i].append(MetaMessage('set_tempo', tempo=Tempo, time=0))
        for j in range(len(long_snd_fin)):
            if j % 2 == 0:
                part4[i].append(
                    Message('note_on', note=long_snd_fin[j], velocity=long_snd_v[j] - 10, time=long_snd_t[j]))
            else:
                part4[i].append(
                    Message('note_on', note=long_snd_fin[j], velocity=long_snd_v[j], time=long_snd_t[j]))

    Filename = "MuseLab_Song.mid"
    Filename = check_filename_available(Filename)
    New_mid.save('./music/Output/' + Filename)
    File_Position = './music/Output/' + Filename
    Input_Position = './music/Output/' + Input_File_name
    MuseScore = check_Sys_and_Open_File(File_Position, Input_Position)
    return MuseScore
    # Open the output through MuseScore in different system

