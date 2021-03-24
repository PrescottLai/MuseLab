from music21 import *
from mido import MidiFile


def Get_SolFa_Name(fp):
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
    if input_key.tonic.name == 'C' and ((input_key.mode == 'major') or (input_key.mode == 'minor')):
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

    if (input_key.tonic.name == 'C#' or input_key.tonic.name == 'Db') and input_key.mode == 'major':
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 1:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 3:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 5:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 6:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 8:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 10:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 0:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if input_key.tonic.name == 'D' and input_key.mode == 'major':
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 2:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 4:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 6:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 7:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 9:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 11:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 1:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if (input_key.tonic.name == 'D#' or input_key.tonic.name == 'Eb') and input_key.mode == 'major':
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 3:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 5:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 7:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 8:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 10:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 0:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 2:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if input_key.tonic.name == 'E' and input_key.mode == 'major':
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 4:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 6:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 8:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 9:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 11:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 1:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 3:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if (input_key.tonic.name == 'E#' or input_key.tonic.name == 'F') and input_key.mode == 'major':
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 5:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 7:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 9:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 10:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 0:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 2:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 4:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if (input_key.tonic.name == 'F#' or input_key.tonic.name == 'Gb') and input_key.mode == 'major':
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 6:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 8:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 10:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 11:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 1:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 3:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 5:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if input_key.tonic.name == 'G' and input_key.mode == 'major':
        # print("YEAH")
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 7:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 9:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 11:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 0:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 2:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 4:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 6:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if (input_key.tonic.name == 'G#' or input_key.tonic.name == 'Ab') and input_key.mode == 'major':
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 8:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 10:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 0:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 1:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 3:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 5:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 7:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if input_key.tonic.name == 'A' and input_key.mode == 'major':
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 9:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 11:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 1:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 2:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 4:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 6:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 8:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if (input_key.tonic.name == 'A#' or input_key.tonic.name == 'Bb') and input_key.mode == 'major':
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 10:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 0:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 2:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 3:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 5:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 7:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 9:
                si_list.append(note_list[0][j])
                order_list.append(7)

    if input_key.tonic.name == 'B' and input_key.mode == 'major':
        for j in range(len(note_list[0])):
            if note_list[0][j] % 12 == 11:
                do_list.append(note_list[0][j])
                order_list.append(1)
            elif note_list[0][j] % 12 == 1:
                re_list.append(note_list[0][j])
                order_list.append(2)
            elif note_list[0][j] % 12 == 3:
                mi_list.append(note_list[0][j])
                order_list.append(3)
            elif note_list[0][j] % 12 == 4:
                fa_list.append(note_list[0][j])
                order_list.append(4)
            elif note_list[0][j] % 12 == 6:
                so_list.append(note_list[0][j])
                order_list.append(5)
            elif note_list[0][j] % 12 == 8:
                la_list.append(note_list[0][j])
                order_list.append(6)
            elif note_list[0][j] % 12 == 10:
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
