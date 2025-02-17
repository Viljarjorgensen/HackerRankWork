def minion_game(string):
    vowels = "AEIOU"
    word = string.strip().upper()
    kevin_score = 0
    stuart_score = 0

    for i in range(len(word)):
        if word[i] in vowels:
            kevin_score += len(word) - i
        else:  # If it's a consonant
            stuart_score += len(word) - i

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == "__main__":
    print(minion_game("BANNANA"))
