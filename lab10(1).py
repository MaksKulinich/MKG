file1 = open('input.txt', 'r', encoding='utf-8')
file2 = open('digit.txt', 'w')
file3 = open('symbols.txt', 'w')
read_file1 = file1.read().split()
for word in read_file1:
    r_word = ''
    for letter in word:
        if letter.isalpha():
            r_word+= letter
    file3.write(r_word + " ")
for word in read_file1:
    numb = ''
    for cifr in word:
        if cifr.isdigit():
            numb += cifr
    file2.write(numb)
file1.close()
file2.close()
file3.close()            