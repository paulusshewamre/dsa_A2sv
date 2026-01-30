remix = input()

words = [word for word in remix.split("WUB") if word]
original = " ".join(words)
print(original)