
from aocd import get_data, submit
lines = get_data(day=1, year=2023).splitlines()
all_numbers = ['0','1','2','3','4','5','6','7','8','9']
dict_words = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7, 'eight':8, 'nine' :9}

#convert all dict_words to numbers in lines

def a():
    nr_list = []
    for line in lines:
        
        found_number = []
        for letter in line:
            if letter in all_numbers:
                found_number.append(letter)

        # print(found_number)
        nr_list.append(int(found_number[0]+found_number[-1]))

    result = sum(nr_list)

    print(nr_list)
    print(result)

    #part1
    #submit(result, part="a", day=1, year=2023)

def b():
    nr_list = []
    for line in lines:
        first = None
        check_letters = ""
        for letter in line:
            if letter.isdigit():
                first = letter
                break
            check_letters += letter
            for letter in check_letters:
                for word, nr in dict_words.items():
                    if word in check_letters:
                        first = str(nr)
                        break
            if first:
                break

        # find last number in line
        last = None
        check_letters = ""
        for letter in reversed(line):
            if letter.isdigit():
                last = letter
                break
            check_letters = letter + check_letters
            for letter in check_letters:
                for word, nr in dict_words.items():
                    if word in check_letters:
                        last = str(nr)
                        break
            if last:
                break

        nr_list.append(int(first+last))


    for i in range(len(nr_list)):
        print(f"{lines[i]}: {nr_list[i]}")
    result = sum(nr_list)
    print(result)

    #part2
    submit(result, part="b", day=1, year=2023)
    #fourfourpsckl47xdbncvndrthree


b()


# 53616c7465645f5fa41015f173ba571605de097bbaaee9f915b0baf67bf16482df805d9fed5bcfa84503003c86d26278592dad94f091b3a6932699a3e0e5c268
