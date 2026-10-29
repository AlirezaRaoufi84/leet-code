# 3- Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        for i in range(len(s)):
            charHolder = []

            for j in range(i, len(s)):
                if s[j] in charHolder:
                    break
                charHolder.append(s[j])

            longest = max(longest, len(charHolder))

        return longest


print(Solution().lengthOfLongestSubstring("abcabcbb"))  # 3

# high runtime.. edit for better runtime :)
