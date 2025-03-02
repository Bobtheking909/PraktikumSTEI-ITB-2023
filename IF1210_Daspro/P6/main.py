##### Soal 1
# import tester

# tester.start("input.txt")
# file = open("input.txt", "r")

# depth = int(file.readline())
# if depth < 0: depth = 0
# print("Jumlah layer:", depth)

# for i in range(depth):
#    print()
#    act = file.readline().strip()
#    n = int(file.readline())
#    weight = []
#    for j in range(n):
#        weight += file.readline().strip("\n").split(" ")
#    bias = file.readline().strip("\n").split(" ")
#    print("Layer ke-" + str(i+1))
#    print("Fungsi aktivasi:", act)
#    print("Jumlah neuron:", n)
#    print("Weight neuron:", weight)
#    print("Bias:", bias)

# file.close()
# tester.end("input.txt")

##### Soal 2
# import tester
# tester.start("output.txt")
# kalimat = input()
# ctr_a, ctr_i, ctr_u, ctr_e, ctr_o = 0, 0, 0, 0, 0
# count = 0
# text = ""
# for huruf in kalimat:
#    if (huruf == "."):
#        break
#    text += huruf
#    if huruf in "Aa":
#        ctr_a += 1
#    if huruf in "Ii":
#        ctr_i += 1
#    if huruf in "Uu":
#        ctr_u += 1
#    if huruf in "Ee":
#        ctr_e += 1
#    if huruf in "Oo":
#        ctr_o += 1
# count = ctr_a + ctr_i + ctr_u + ctr_e + ctr_o

# if (count == 0): text = "Tidak ada huruf"

# file = open("output.txt", "w")
# file.write(str(ctr_a))
# file.write(str(ctr_i))
# file.write(str(ctr_u))
# file.write(str(ctr_e))
# file.write(str(ctr_o))
# file.write("\n")
# file.write(str(count))
# file.write("\n")
# file.write(text)
# file.close()
# tester.end("output.txt")


##### Soal 3
# import tester

# tester.start("input.csv")
# file = open("input.csv", "r")

# def sort(arr):
#    for i in range (len(arr)):
#        for j in range (len(arr)):
#            if (arr[j] > arr[i]):
#                temp = arr[j]
#                arr[j] = arr[i]
#                arr[i] = temp
#    return arr

# data = []
# for text in file:
#    row = text.strip("\n")
#    data.append(row.split(","))
# lulus = 0
# min_umur_1 = 9999
# arr_umur = []
# for i in range (1, len(data)):
#    if (int(data[i][3]) > 75):
#        lulus += 1
#    arr_umur.append(data[i][2])

# arr_min = sort(arr_umur)

# print(lulus)
# print(arr_min[1])
# file.close()

# tester.end("input.csv")


##### Soal 4
# import tester
# tester.start("input.csv")

# file = open("input.csv", "r")
# lines = file.readlines()
# departments = []
# salaries = []
# for line in lines[1:]:
#     #membaca tiap line
#     line_data = line.strip().split(",")
#     #bila tidak ada dalam departemen (belum dicatat) dimasukkan di dalam array departemen
#     if line_data[1] not in departments:
#         departments.append(line_data[1])
#         #sama dengan salarynya juga
#         salaries.append(int(line_data[2]))
# else:
#         #jika ada, maka menambahkan salary departemen tersebut
#         index = departments.index(line_data[1])
#         salaries[index] += int(line_data[2])

# if len(salaries) == 0: 
#     #handle file kosong
#     print("Data kosong")
# else: 
#     for salary in salaries: 
#         print(salary)
#     print(sum(salaries)//len(salaries))

# tester.end("input.csv")


##### Soal 5
# def count_words(row):
#   words = row.split()
#   word_count = []

#   for word in words:
#     found = False # flag

#     for wc in word_count:
#       if wc[0] == word:
#         wc[1] += 1
#         found = True
#         break
#    if not found:
#       word_count.append([word, 1])
# return word_count

# def find_common_words(list1, list2):
#   common_words = []

#   for word1, freq1 in list1:
#     for word2, freq2 in list2:
#       if word1 == word2:
#         common_words.append((word1, freq1, freq2))

#   return common_words

# def main():
#   file = open("input.txt", "r")

#   row1 = file.readline().strip()
#   row2 = file.readline().strip()

#   file.close()

#   list1 = count_words(row1)
#   list2 = count_words(row2)

#   common_words = find_common_words(list1, list2)
#   if not common_words:
#     print("Tidak ada kata yang sama")
#   else:
#     for word, freq1, freq2 in common_words:
#       print("{},{},{}".format(word, freq1, freq2))

# import tester

# tester.start("input.txt")
# if __name__ == "__main__":
#   main()
# tester.end("input.txt")

    







