import csv
article_file = open("article.txt", 'r', encoding='utf-8')
article_lower = article_file.read().lower()
article_split= article_lower.split(" ")
csv_file = open("numbers.csv", 'w')
writer = csv.writer(csv_file)
words = input("Введіть слова ")
words_split = words.split(" ")
for i in words_split:
    if i in article_split:
        x = article_split.count(i)
        writer.writerow([i + "-" + str(x)])
article_file.close()
csv_file.close()            
