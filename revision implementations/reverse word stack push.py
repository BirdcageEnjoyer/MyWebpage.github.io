#take an input, initialise a list, push the characters of the input in reverse order on to stack, followed by how many characters the input is

input = input("enter a word to push")
wordLength = len(input)
myStack = [None for i in range(wordLength+1)]
pointer = wordLength

for _ in range(wordLength):
    if pointer > -1:
        myStack[_] = input[pointer-1]
        pointer -= 1

myStack[-1] = wordLength


print(myStack)