def get_triangle_value(word):
    running_total = 0
    for char in word:
        running_total += ord(char) - 64

    return running_total


f = open("C:\\Euler\\p042_words.txt", "r")
for line in f:
  line = line.replace('"', '')

a_words = line.split(",")
word_dict = {}
max_word_value = 0
for word in a_words:
    triangle_value = get_triangle_value(word)
    word_dict[word] = triangle_value
    if triangle_value > max_word_value:
        max_word_value = triangle_value

triangle_values = []
tri_val = 0
n = 1
while tri_val < max_word_value:
    tri_val = int(0.5 * n * (n + 1))
    triangle_values.append(tri_val)
    n += 1

print(triangle_values)
print(word_dict)
print(max_word_value)

counter = 0
for word, value in word_dict.items():
    if value in triangle_values:
        print(value)
        counter += 1

print(counter)
