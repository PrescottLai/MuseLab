from mido import Message, MidiFile, MidiTrack
from music21 import *


def Add_Base_Chords_type1(fp1, fp2):
    Base_mid = MidiFile(fp2)  # sChords
    mid = MidiFile(fp1)
    list_c, list_v_temp, list_v, list_n_temp, list_n, list_t, channel_list, note_list, velocity_list, time_list = \
        [], [], [], [], [], [], [], [], [], []
    print(Base_mid)
    print("3rd_mid_info: ", mid)
    # --------------------------------Grab the note number from original midi file------------------------------------
    z = 0
    for msg in mid.tracks[0]:
        if msg.type == 'note_on':
            list_c.append(msg.channel)
            list_t.append(msg.time)
            z += 1
            print("3rd_msg:", z, msg)
            # C-A(m3),D-B(m3),E-C(M3),F-D(m3),G-E(m3),A-F(M3),B-G(M3) m3: -3 M3:-4
    for j in range(len(list_t)):
        time_list.append(list_t.pop(0))
        for i in range(2):
            time_list.append(0)
    channel_list.append(list_c)
    adding_num = 0
    z = 0
    for msg in Base_mid.tracks[0]:
        if adding_num == 3:
            adding_num = 0
            for i in range(3):
                list_n.append(list_n_temp[i])
                list_v.append(list_v_temp[i])
            for i in range(3):
                list_n.append(list_n_temp.pop(0))
                list_v.append(list_v_temp.pop(0))
        elif msg.type == 'note_on' and adding_num != 3:
            list_n_temp.append(msg.note)
            list_v_temp.append(msg.velocity)
            adding_num += 1
            z += 1
            print("sChords_msg:", z, msg)
    velocity_list.append(list_v)
    note_list.append(list_n)  # 注意：一整个list append， 所以调用的时候要用 note_list[][]
    # ------------------------------------Checking and Debug--------------------------------------
    print("N_List: ", note_list[0])

    print("Type of T_List_Info: ", type(time_list[0]))
    # print("N_List: ", note_list[1])
    print("V_List: ", velocity_list[0])
    # print("V_List: ", velocity_list[1])
    print("T_List: ", time_list)
    # print("T_List: ", time_list[1])
    print("MIDI data: ", Base_mid)
    print("Mid_Track_Length: ", len(Base_mid.tracks))
    print("N_List_Length: ", len(note_list[0]))
    print("T_List_Length: ", len(time_list))
    print("V_List_Length: ", len(velocity_list[0]))
    # --------------------------------Put the note number Back to original midi file------------------------------------
    Base_track = MidiTrack()
    print("Type_Of_Track: ", type(Base_track))
    mid.tracks.append(Base_track)
    Base_track.append((Message('program_change', channel=2, program=0, time=0)))
    for j in range(len(velocity_list[0])):
        Base_track.append(Message('note_on', note=note_list[0][j], velocity=velocity_list[0][j], time=time_list[j]))
    print("Type1 Re-Orchestrating.........\n")
    mid.save('./music/Output/Type1/NEW_Song_Type1.mid')
    NEW = converter.parse('./music/Output/Type1/NEW_Song_Type1.mid')
    NEW.write("xml", "./music/Output/Type1/NEW_Song_Type1.xml")
    NEW.write("midi", "./music/Output/Type1/NEW_Song_Type1.mid")
    NEW_Song_Type1 = converter.parse('./music/Output/Type1/NEW_Song_Type1.mid')
    # NEW_Song_Type1.show()
    print(type(NEW_Song_Type1.analyze('key')))
    output_key = NEW_Song_Type1.analyze('key')
    print(output_key.tonic.name, output_key.mode)
    mid3 = MidiFile('./music/Output/Type1/NEW_Song_Type1.mid')
    print(len(mid3.tracks))
    for i in range(len(mid3.tracks)):
        print("Track: ", i)
        z = 0
        for msg in mid3.tracks[i]:
            if msg.type == 'note_on':
                z += 1
                print("New_Song_Type1_msg:", z, msg)
        print("Type1 Re-Orchestration Success!!")


def Add_Base_Chords_type2(fp1, fp2):
    Base_mid = MidiFile(fp2)  # sChords
    mid = MidiFile(fp1)
    list_c, list_v_temp, list_v, list_n_temp, list_n, list_t, channel_list, note_list, velocity_list, time_list = \
        [], [], [], [], [], [], [], [], [], []
    print(Base_mid)
    print("3rd_mid_info: ", mid)
    # --------------------------------Grab the note number from original midi file------------------------------------
    z = 0
    for msg in mid.tracks[0]:
        if msg.type == 'note_on':
            list_c.append(msg.channel)
            list_t.append(msg.time)
            z += 1
            print("3rd_msg:", z, msg)
            # C-A(m3),D-B(m3),E-C(M3),F-D(m3),G-E(m3),A-F(M3),B-G(M3) m3: -3 M3:-4
    for j in range(len(list_t)):
        time_list.append(list_t.pop(0))
        for i in range(1):
            time_list.append(0)
    channel_list.append(list_c)
    adding_num = 0
    z = 0
    for msg in Base_mid.tracks[0]:
        if adding_num == 2:
            adding_num = 0
            for i in range(2):
                list_n.append(list_n_temp[i])
                list_v.append(list_v_temp[i])
            for i in range(2):
                list_n.append(list_n_temp.pop(0))
                list_v.append(list_v_temp.pop(0))
        elif msg.type == 'note_on' and adding_num != 2:
            list_n_temp.append(msg.note)
            list_v_temp.append(msg.velocity)
            adding_num += 1
            z += 1
            print("sChords_msg:", z, msg)
    velocity_list.append(list_v)
    note_list.append(list_n)  # 注意：一整个list append， 所以调用的时候要用 note_list[][]
    # ------------------------------------Checking and Debug--------------------------------------
    print("N_List: ", note_list[0])

    print("Type of T_List_Info: ", type(time_list[0]))
    print("V_List: ", velocity_list[0])
    print("T_List: ", time_list)
    print("MIDI data: ", Base_mid)
    print("Mid_Track_Length: ", len(Base_mid.tracks))
    print("N_List_Length: ", len(note_list[0]))
    print("T_List_Length: ", len(time_list))
    print("V_List_Length: ", len(velocity_list[0]))
    # --------------------------------Put the note number Back to original midi file------------------------------------
    Base_track = MidiTrack()
    print("Type_Of_Track: ", type(Base_track))
    mid.tracks.append(Base_track)
    Base_track.append((Message('program_change', channel=2, program=0, time=0)))
    for j in range(len(velocity_list[0])):
        Base_track.append(Message('note_on', note=note_list[0][j], velocity=velocity_list[0][j], time=time_list[j]))
    print("Type2 Re-Orchestrating.........\n")
    mid.save('./music/Output/Type2/NEW_Song_Type2.mid')
    NEW = converter.parse('./music/Output/Type2/NEW_Song_Type2.mid')
    NEW.write("midi", "./music/Output/Type2/NEW_Song_Type2.mid")
    NEW_Song_Type2 = converter.parse('./music/Output/Type2/NEW_Song_Type2.mid')
    # NEW_Song_Type2.show()
    NEW.write("xml", "./music/Output/Type2/NEW_Song_Type2.xml")
    print(type(NEW_Song_Type2.analyze('key')))
    output_key = NEW_Song_Type2.analyze('key')
    print(output_key.tonic.name, output_key.mode)
    mid3 = MidiFile('./music/Output/Type2/NEW_Song_Type2.mid')
    print(len(mid3.tracks))
    for i in range(len(mid3.tracks)):
        print("Track: ", i)
        z = 0
        for msg in mid3.tracks[i]:
            if msg.type == 'note_on':
                z += 1
                print("New_Song_Type2_msg:", z, msg)
    print("Type2 Re-Orchestration Success!!")

# def Add_Base_Chords_type3(fp1, fp2):
#     Base_mid = MidiFile(fp2) #sChords
#     mid = MidiFile(fp1) #3rd
#     list_c, list_v_temp, list_v, list_n_temp, list_All_n, \
#     list_t, channel_list, note_list, velocity_list, time_list = \
#          [], [], [], [], [], [], [], [], [], []
#     a = 0
#     print(Base_mid)
#     print(mid)
#     # --------------------------------Grab the msg number from original midi file------------------------------------
#     for msg in mid.tracks[0]:
#         if msg.type == 'note_on':
#             list_c.append(msg.channel)
#             list_v.append(msg.velocity)
#     channel_list.append(list_c)
#     print("All_Velocity_List: ", list_v)
#     adding_num = 0
#     # ---------------------------------------------把所有的和弦里的音的midi number 放在一个list 里-------------------------
#     for msg in Base_mid.tracks[0]:
#         if adding_num == 3:
#             adding_num = 0
#             for i in range(3):
#                 list_All_n.append(list_n_temp[i])
#                 list_v.append(list_v_temp[i])
#             for i in range(3):
#                 list_All_n.append(list_n_temp.pop(0))
#                 list_v.append(list_v_temp.pop(0))
#         elif msg.type == 'note_on' and adding_num != 3:
#             list_n_temp.append(msg.note)
#             list_v_temp.append(msg.velocity)
#             adding_num += 1
#             print("sChords_msg: ", msg)
#     print("All_Note_List: ", list_All_n)
#     # -------------------------------------------只保留每一小节前面的第一个和弦的note & Velocity，以用于做长音base-------------------
#     adding_num = 0
#     x = 0
#     while x < len(list_All_n):
#         if adding_num == 6:
#             adding_num = 0
#             x += 18
#         if x > len(list_All_n): break
#         note_list.append(list_All_n[x])
#         velocity_list.append(list_v[x])
#         adding_num += 1
#         x += 1
#     # x = 0
#     # while x < len(list_v):
#     #     for i in range(6):
#     #         velocity_list.append(list_v[x])
#     #         i+=1
#     #     x+=8
#     # ------------------------------------------制作全音符 time list-----------------------------------------------------
#     x = 0
#     while x < len(note_list)-1:
#         if x < 6:
#             x += 6
#             for i in range(2):
#                 time_list.append(1920)
#                 time_list.append(0)
#                 time_list.append(0)
#         elif x % 2 == 0:
#             time_list.append(25)
#             time_list.append(0)
#             time_list.append(0)
#             x += 3
#         elif x % 2 == 1:
#             time_list.append(1920)
#             time_list.append(0)
#             time_list.append(0)
#             x += 3
#
#     print(time_list)
#     # -----------------------------------Checking and Debug-----------------------------------------------------
#     print("N_List: ", note_list)
#
#     # print("N_List: ", note_list[1])
#     print("V_List: ", velocity_list)
#     # print("V_List: ", velocity_list[1])
#     print("T_List: ", time_list)
#     # print("T_List: ", time_list[1])
#     print("MIDI data: ", Base_mid)
#     print("Mid_Track_Length: ", len(Base_mid.tracks))
#     print("N_List_Length: ", len(note_list))
#     print("T_List_Length: ", len(time_list))
#     print("V_List_Length: ", len(velocity_list))
#     # --------------------------------Put the note number Back to original midi file---------------------------------
#     Base_track = MidiTrack()
#     print("Type_Of_Track: ", type(Base_track))
#     mid.tracks.append(Base_track)
#     for j in range(len(velocity_list)):
#         Base_track.append(Message('note_on', note=note_list[j], velocity=velocity_list[j], time=time_list[j]))
#
#     mid.save('./music/Output/NEW_Song_Type2.mid')
#     NEW = converter.parse('./music/Output/NEW_Song_Type2.mid')
#     NEW.show()
#     NEW.write("xml", "./music/Output/NEW_Song_Type2.xml")
#     print(type(NEW.analyze('key')))
#     key = NEW.analyze('key')
#     print(key.tonic.name, key.mode)
#     mid3 = MidiFile('./music/Output/NEW_Song_Type2.mid')
#     print(len(mid3.tracks))
#     for i in range(len(mid3.tracks)):
#         print("Track: ", i)
#         z = 0
#         for msg in mid3.tracks[i]:
#             if msg.type == 'note_on':
#                 z+=1
#                 print("New_Song_Type2_msg:",z, msg)
