import sys


def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <sentence1> <sentence2>")
        sys.exit(1)

    frase1 = sys.argv[1]
    frase2 = sys.argv[2]

    if is_anagram(frase1, frase2):
        print("sentences are  anagrams.")
    else:
        print("sentences are not anagrams.")


if __name__ == "__main__":
    main()
