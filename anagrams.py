# Given two strings determine whether they are anagrams.

from typing import List, Dict

def is_anagram_naive(str1: str, str2: str) -> bool:
    lst1: List[str] = sorted(list(str1))
    lst2: List[str] = sorted(list(str2))
    return lst1 == lst2

def is_anagram(str1: str, str2: str) -> bool:
    count: Dict[str,int] = {}

    for chr1 in list(str1):
        if chr1 in count:
            count[chr1] += 1
        else:
            count[chr1] = 1

    for chr2 in list(str2):
        if chr2 in count:
            count[chr2] -= 1
        else:
            return False

    return sum(count.values()) == 0

if __name__ == "__main__":
    print("wen", "new", is_anagram("wen", "new"))
    print("wen", "one", is_anagram("wen", "one"))
