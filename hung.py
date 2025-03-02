# Hungman Game
# Possible only for non repeated letters in the word

# original = [ 'p', 'y','t','h','o','n']

string_input = input("Player 1 --> Enter the Word with spaces btw letters: ")
original = string_input.split()
# print(original)

# to_be_filled = ['_', '_', '_', '_', '_', '_']
to_be_filled = ['_' for _ in original]
# print(to_be_filled)

while original != to_be_filled:

    print(' '.join(to_be_filled))

    guess = input("Player 2 --> Enter the guessed Letter: ")

    if str(guess) in original:
        to_be_filled[original.index(guess)] = guess
        print("Yes")
    else:
        print("No")

print(' '.join(to_be_filled))
print("Hoorayyy!!! You have guessed the word correctly.")
    