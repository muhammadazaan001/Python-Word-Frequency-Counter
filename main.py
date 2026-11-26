print("------Welcome to Words Frequency Counter-----")

text = input("Enter your text: ")
words = text.split()

frequency = {
    }

for word in words:
    if word not in frequency:
        frequency[word] = 1
    else:
        frequency[word]+=1

print("Word frequency:")

for key, value in frequency.items():
    print(f"{key}: {value}")


    
    
