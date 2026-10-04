import string

def clean_text(text):
    return ''.join(
        ch.lower()
        for ch in text
        if ch.isalnum()
    )

def is_anagram_sorting(text1, text2):
    text1 = clean_text(text1)
    text2 = clean_text(text2)

    return sorted(text1) == sorted(text2)

def character_count(text):
    count = {}

    for ch in clean_text(text):
        count[ch] = count.get(ch, 0) + 1

    return count


def is_anagram_dictionary(text1, text2):
    return character_count(text1) == character_count(text2)

def anagram_key(text):
    cleaned = clean_text(text)
    return tuple(sorted(cleaned))

word1 = input("Enter first word or phrase: ")
word2 = input("Enter second word or phrase: ")

if is_anagram_sorting(word1, word2):
    print("\nUsing sorting: Anagram")
else:
    print("\nUsing sorting: Not an Anagram")

if is_anagram_dictionary(word1, word2):
    print("Using dictionary: Anagram")
else:
    print("Using dictionary: Not an Anagram")

print("\nTuple Key 1:", anagram_key(word1))
print("Tuple Key 2:", anagram_key(word2))

words = [
    "listen",
    "silent",
    "enlist",
    "evil",
    "vile",
    "live",
    "veil",
    "hello"
]

anagram_groups = {}

for word in words:
    key = anagram_key(word)

    if key not in anagram_groups:
        anagram_groups[key] = []

    anagram_groups[key].append(word)


print("\nAnagram Groups:")
for key, group in anagram_groups.items():
    if len(group) > 1:
        print(group)