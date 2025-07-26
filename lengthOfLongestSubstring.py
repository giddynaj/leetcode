def lengthOfLongestSubstring(self, s):
    seen_letters = {}
    left, right = 0, 0
    longest_substring = 0

    while (right < len(s)):
        seen_letters[s[right]] = seen_letters.get(s[right], 0) + 1
        while(seen_letters[s[right]] > 1):
            seen_letters[s[left]] -= 1
            left += 1
        current_substring_len = right - left + 1
        if (current_substring_len > longest_substring):
            longest_substring = current_substring_len
        right += 1
    return longest_substring
