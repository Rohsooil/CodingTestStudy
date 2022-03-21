def solution(m, music_info_list):
    m = m.replace('C#', 'K')
    m = m.replace('D#', 'L')
    m = m.replace('F#', 'M')
    m = m.replace('A#', 'N')
    m = m.replace('G#', 'O')

    def time_gap(start, end):
        start_minute = int(start[0]) * 60 + int(start[1])
        end_minute = int(end[0]) * 60 + int(end[1])
        return end_minute - start_minute

    answer_map = {}
    answer = ''
    for music_info in music_info_list:
        info_list = music_info.split(',')
        info_list[3] = info_list[3].replace('C#', 'K')
        info_list[3] = info_list[3].replace('D#', 'L')
        info_list[3] = info_list[3].replace('F#', 'M')
        info_list[3] = info_list[3].replace('A#', 'N')
        info_list[3] = info_list[3].replace('G#', 'O')
        play_time = time_gap(info_list[0].split(':'), info_list[1].split(':'))
        repeats = (play_time // len(info_list[3]), play_time % len(info_list[3]))
        melody = info_list[3] * repeats[0] + info_list[3][:repeats[1]]
        if m in melody:
            print(play_time)
            if play_time in answer_map:
                answer_map[play_time].append(info_list[2])
            else:
                answer_map[play_time] = [info_list[2]]

    if not answer_map:
        return '(None)'

    max_length = max(answer_map.keys())
    print(max_length)
    return answer_map[max_length][0]


# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABC", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:14,WORLD,ABCDEF"]))
