from pprint import pprint
sentence = "This is a common interview question"
storage = {}
for char in sentence:
    if char in storage:
        storage[char] += 1
    else:
        storage[char] = 1
# print(storage)
sort = storage.items()


# print(storage)
sorted_freq = sorted(sort, key=lambda kv: kv[1], reverse=True)
print(sorted_freq[0])
