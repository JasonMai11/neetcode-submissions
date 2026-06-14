class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # counter -> O(N)

        # basic implementation
        hashmap = {}
        for char in s:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1

        for char in t:
            if char not in hashmap:
                return False
            else:
                hashmap[char] -= 1
                if hashmap[char] < 0:
                    return False

        for i in hashmap:
            if hashmap[i] > 0:
                return False
        
        return True