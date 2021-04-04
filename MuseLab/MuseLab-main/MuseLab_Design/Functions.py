import random
from music21 import *
from mido import MidiFile


def Get_SolFa_Name_Order(fp):
    s = converter.parse(fp)
    mid = MidiFile(fp)

    list_n = []
    note_list = []
    print(mid)
    # --------------------------------Grab the note number from original midi file------------------------------------
    for i in range(len(mid.tracks)):
        for msg in mid.tracks[i]:
            if msg.type == 'note_on' or msg.type == 'note_off':
                list_n.append(msg.note)
            if msg.type == 'key_signature':
                k = msg.key
                print(k)
                # C-A(m3),D-B(m3),E-C(M3),F-D(m3),G-E(m3),A-F(M3),B-G(M3) m3: -3 M3:-4
        i += 1
        note_list.append(list_n)
    # ------------------------------Change the note number by some musical rules for adding the base------------------
    do_list, re_list, mi_list, fa_list, so_list, la_list, si_list = [], [], [], [], [], [], []
    all_list, order_list = [], []
    input_key = s.analyze('key')
    input_key.tonic.name = k
    print("SolFa_Name.py key name and mode:")
    print(input_key.tonic.name, input_key.mode)
    # key.mode = 'major'
    if input_key.tonic.name == 'C' and\
            ((input_key.mode == 'major') or (input_key.mode == 'minor')):
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 0:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 2:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 4 or note_list[0][j] % 12 == 3:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 5:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 7:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 9 or note_list[0][j] % 12 == 8:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 11 or note_list[0][j] % 12 == 10:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if (input_key.tonic.name == 'C#' or input_key.tonic.name == 'Db') and\
            ((input_key.mode == 'major') or (input_key.mode == 'minor')):
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 1:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 3:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 5 or note_list[0][j] % 12 == 4:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 6:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 8:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 10 or note_list[0][j] % 12 == 9:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 0 or note_list[0][j] % 12 == 11:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if input_key.tonic.name == 'D' and\
            ((input_key.mode == 'major') or (input_key.mode == 'minor')):
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 2:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 4:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 6 or note_list[0][j] % 12 == 5:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 7:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 9:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 11 or note_list[0][j] % 12 == 10:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 1 or note_list[0][j] % 12 == 0:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if (input_key.tonic.name == 'D#' or input_key.tonic.name == 'Eb') and\
            ((input_key.mode == 'major') or (input_key.mode == 'minor')):
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 3:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 5:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 7 or note_list[0][j] % 12 == 6:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 8:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 10:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 0 or note_list[0][j] % 12 == 11:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 2 or note_list[0][j] % 12 == 1:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if input_key.tonic.name == 'E' and\
            ((input_key.mode == 'major') or (input_key.mode == 'minor')):
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 4:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 6:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 8 or note_list[0][j] % 12 == 7:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 9:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 11:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 1 or note_list[0][j] % 12 == 0:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 3 or note_list[0][j] % 12 == 2:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if (input_key.tonic.name == 'E#' or input_key.tonic.name == 'F') and\
            ((input_key.mode == 'major') or (input_key.mode == 'minor')):
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 5:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 7:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 9 or note_list[0][j] % 12 == 8:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 10:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 0:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 2 or note_list[0][j] % 12 == 1:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 4 or note_list[0][j] % 12 == 3:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if (input_key.tonic.name == 'F#' or input_key.tonic.name == 'Gb') and\
            ((input_key.mode == 'major') or (input_key.mode == 'minor')):
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 6:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 8:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 10 or note_list[0][j] % 12 == 9:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 11:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 1:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 3 or note_list[0][j] % 12 == 2:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 5 or note_list[0][j] % 12 == 4:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if input_key.tonic.name == 'G' and\
            ((input_key.mode == 'major') or (input_key.mode == 'minor')):
        # print("YEAH")
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 7:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 9:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 11 or note_list[0][j] % 12 == 10:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 0:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 2:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 4 or note_list[0][j] % 12 == 3:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 6 or note_list[0][j] % 12 == 5:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if (input_key.tonic.name == 'G#' or input_key.tonic.name == 'Ab') and\
            ((input_key.mode == 'major') or (input_key.mode == 'minor')):
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 8:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 10:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 0 or note_list[0][j] % 12 == 11:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 1:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 3:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 5 or note_list[0][j] % 12 == 4:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 7 or note_list[0][j] % 12 == 6:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if input_key.tonic.name == 'A' and\
            ((input_key.mode == 'major') or (input_key.mode == 'minor')):
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 9:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 11:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 1 or note_list[0][j] % 12 == 0:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 2:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 4:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 6 or note_list[0][j] % 12 == 5:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 8 or note_list[0][j] % 12 == 7:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if (input_key.tonic.name == 'A#' or input_key.tonic.name == 'Bb') and\
            ((input_key.mode == 'major') or (input_key.mode == 'minor')):
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 10:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 0:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 2 or note_list[0][j] % 12 == 1:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 3:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 5:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 7 or note_list[0][j] % 12 == 6:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 9 or note_list[0][j] % 12 == 8:
                si_list.append(note_list[0][j])
                order_list.append(7)
    if input_key.tonic.name == 'B' and\
            ((input_key.mode == 'major') or (input_key.mode == 'minor')):

        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 11:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 1:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 3 or note_list[0][j] % 12 == 2:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 4:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 6:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 8 or note_list[0][j] % 12 == 7:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 10 or note_list[0][j] % 12 == 9:
                si_list.append(note_list[0][j])
                order_list.append(7)

    all_list.append(do_list)
    all_list.append(re_list)
    all_list.append(mi_list)
    all_list.append(fa_list)
    all_list.append(so_list)
    all_list.append(la_list)
    all_list.append(si_list)
    all_list.append(order_list)
    return all_list


def Current_SolFa_Name(input_melody_key, key_mode, note_num):
    SolFa_num = 0
    if input_melody_key == 'C' and ((key_mode == 'major') or (key_mode == 'minor')):
        if note_num % 12 == 0:
            SolFa_num = 1
        elif note_num % 12 == 2:
            SolFa_num = 2
        elif note_num % 12 == 4 or note_num % 12 == 3:
            SolFa_num = 3
        elif note_num % 12 == 5:
            SolFa_num = 4
        elif note_num % 12 == 7:
            SolFa_num = 5
        elif note_num % 12 == 9 or note_num % 12 == 8:
            SolFa_num = 6
        elif note_num % 12 == 11 or note_num % 12 == 10:
            SolFa_num = 7

    if (input_melody_key == 'C#' or input_melody_key == 'Db') and ((key_mode == 'major') or (key_mode == 'minor')):
        if note_num % 12 == 1:
            SolFa_num = 1
        elif note_num % 12 == 3:
            SolFa_num = 2
        elif note_num % 12 == 5 or note_num % 12 == 4:
            SolFa_num = 3
        elif note_num % 12 == 6:
            SolFa_num = 4
        elif note_num % 12 == 8:
            SolFa_num = 5
        elif note_num % 12 == 10 or note_num % 12 == 9:
            SolFa_num = 6
        elif note_num % 12 == 0 or note_num % 12 == 11:
            SolFa_num = 7

    if input_melody_key == 'D' and ((key_mode == 'major') or (key_mode == 'minor')):
        if note_num % 12 == 2:
            SolFa_num = 1
        elif note_num % 12 == 4:
            SolFa_num = 2
        elif note_num % 12 == 6 or note_num % 12 == 5:
            SolFa_num = 3
        elif note_num % 12 == 7:
            SolFa_num = 4
        elif note_num % 12 == 9:
            SolFa_num = 5
        elif note_num % 12 == 11 or note_num % 12 == 10:
            SolFa_num = 6
        elif note_num % 12 == 1 or note_num % 12 == 0:
            SolFa_num = 7

    if (input_melody_key == 'D#' or input_melody_key == 'Eb') and ((key_mode == 'major') or (key_mode == 'minor')):
        if note_num % 12 == 3:
            SolFa_num = 1
        elif note_num % 12 == 5:
            SolFa_num = 2
        elif note_num % 12 == 7 or note_num % 12 == 6:
            SolFa_num = 3
        elif note_num % 12 == 8:
            SolFa_num = 4
        elif note_num % 12 == 10:
            SolFa_num = 5
        elif note_num % 12 == 0 or note_num % 12 == 11:
            SolFa_num = 6
        elif note_num % 12 == 2 or note_num % 12 == 1:
            SolFa_num = 7

    if input_melody_key == 'E' and ((key_mode == 'major') or (key_mode == 'minor')):
        if note_num % 12 == 4:
            SolFa_num = 1
        elif note_num % 12 == 6:
            SolFa_num = 2
        elif note_num % 12 == 8 or note_num % 12 == 7:
            SolFa_num = 3
        elif note_num % 12 == 9:
            SolFa_num = 4
        elif note_num % 12 == 11:
            SolFa_num = 5
        elif note_num % 12 == 1 or note_num % 12 == 0:
            SolFa_num = 6
        elif note_num % 12 == 3 or note_num % 12 == 2:
            SolFa_num = 7

    if (input_melody_key == 'E#' or input_melody_key == 'F') and ((key_mode == 'major') or (key_mode == 'minor')):
        if note_num % 12 == 5:
            SolFa_num = 1
        elif note_num % 12 == 7:
            SolFa_num = 2
        elif note_num % 12 == 9 or note_num % 12 == 8:
            SolFa_num = 3
        elif note_num % 12 == 10:
            SolFa_num = 4
        elif note_num % 12 == 0:
            SolFa_num = 5
        elif note_num % 12 == 2 or note_num % 12 == 1:
            SolFa_num = 6
        elif note_num % 12 == 4 or note_num % 12 == 3:
            SolFa_num = 7

    if (input_melody_key == 'F#' or input_melody_key == 'Gb') and ((key_mode == 'major') or (key_mode == 'minor')):
        if note_num % 12 == 6:
            SolFa_num = 1
        elif note_num % 12 == 8:
            SolFa_num = 2
        elif note_num % 12 == 10 or note_num % 12 == 9:
            SolFa_num = 3
        elif note_num % 12 == 11:
            SolFa_num = 4
        elif note_num % 12 == 1:
            SolFa_num = 5
        elif note_num % 12 == 3 or note_num % 12 == 2:
            SolFa_num = 6
        elif note_num % 12 == 5 or note_num % 12 == 4:
            SolFa_num = 7

    if input_melody_key == 'G' and ((key_mode == 'major') or (key_mode == 'minor')):
        if note_num % 12 == 7:
            SolFa_num = 1
        elif note_num % 12 == 9:
            SolFa_num = 2
        elif note_num % 12 == 11 or note_num % 12 == 10:
            SolFa_num = 3
        elif note_num % 12 == 0:
            SolFa_num = 4
        elif note_num % 12 == 2:
            SolFa_num = 5
        elif note_num % 12 == 4 or note_num % 12 == 3:
            SolFa_num = 6
        elif note_num % 12 == 6 or note_num % 12 == 5:
            SolFa_num = 7

    if (input_melody_key == 'G#' or input_melody_key == 'Ab') and ((key_mode == 'major') or (key_mode == 'minor')):
        if note_num % 12 == 8:
            SolFa_num = 1
        elif note_num % 12 == 10:
            SolFa_num = 2
        elif note_num % 12 == 0 or note_num % 12 == 11:
            SolFa_num = 3
        elif note_num % 12 == 1:
            SolFa_num = 4
        elif note_num % 12 == 3:
            SolFa_num = 5
        elif note_num % 12 == 5 or note_num % 12 == 4:
            SolFa_num = 6
        elif note_num % 12 == 7 or note_num % 12 == 6:
            SolFa_num = 7

    if input_melody_key == 'A' and ((key_mode == 'major') or (key_mode == 'minor')):
        if note_num % 12 == 9:
            SolFa_num = 1
        elif note_num % 12 == 11:
            SolFa_num = 2
        elif note_num % 12 == 1 or note_num % 12 == 0:
            SolFa_num = 3
        elif note_num % 12 == 2:
            SolFa_num = 4
        elif note_num % 12 == 4:
            SolFa_num = 5
        elif note_num % 12 == 6 or note_num % 12 == 5:
            SolFa_num = 6
        elif note_num % 12 == 8 or note_num % 12 == 7:
            SolFa_num = 7

    if (input_melody_key == 'A#' or input_melody_key == 'Bb') and ((key_mode == 'major') or (key_mode == 'minor')):
        if note_num % 12 == 10:
            SolFa_num = 1
        elif note_num % 12 == 0:
            SolFa_num = 2
        elif note_num % 12 == 2 or note_num % 12 == 1:
            SolFa_num = 3
        elif note_num % 12 == 3:
            SolFa_num = 4
        elif note_num % 12 == 5:
            SolFa_num = 5
        elif note_num % 12 == 7 or note_num % 12 == 6:
            SolFa_num = 6
        elif note_num % 12 == 9 or note_num % 12 == 8:
            SolFa_num = 7

    if input_melody_key == 'B' and ((key_mode == 'major') or (key_mode == 'minor')):
        if note_num % 12 == 11:
            SolFa_num = 1
        elif note_num % 12 == 1:
            SolFa_num = 2
        elif note_num % 12 == 3 or note_num % 12 == 2:
            SolFa_num = 3
        elif note_num % 12 == 4:
            SolFa_num = 4
        elif note_num % 12 == 6:
            SolFa_num = 5
        elif note_num % 12 == 8 or note_num % 12 == 7:
            SolFa_num = 6
        elif note_num % 12 == 10 or note_num % 12 == 9:
            SolFa_num = 7

    return SolFa_num


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
