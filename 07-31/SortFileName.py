def solution(files):
    answer = []
    split_file_list = []

    def split_file_names(file_name, idx):
        add_number = False
        head, number, tail = '', '', ''
        for ch in file_name:
            if ch.isnumeric() and not number:
                add_number = True
            elif not ch.isnumeric() and number:
                add_number = False

            if add_number:
                number += ch
            elif not add_number and not number:
                head += ch
            else:
                tail += ch

        return head, number, tail, idx

    for i, file in enumerate(files):
        split_file_list.append(split_file_names(file, i))

    split_file_list.sort(key=lambda x: (x[0].lower(), int(x[1]), x[3]))
    for split_file in split_file_list:
        answer.append(files[split_file[3]])

    return answer


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
