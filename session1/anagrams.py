import sys

def anagram(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    count = {}

    for idx in range(len(str1)):
        char1 = str1[idx]
        char2 = str2[idx]
        count[char1] = count.get(char1, 0) + 1
        count[char2] = count.get(char2, 0) - 1

        if count[char1] == 0:
            count.pop(char1)
        if char2 in count and count[char2] == 0:
            count.pop(char2)

    return len(count) == 0

def main() -> int:
    """Echo the input arguments to standard output"""
    print(f"Anagram: {anagram('blah', 'hlab') =}")
    print(f"Anagram: {anagram('foo', 'boo') =}")
    print(f"Anagram: {anagram('foo', 'alice') =}")
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit