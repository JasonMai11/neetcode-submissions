class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> map = new HashSet<>();
        int longest = 0;
        int l = 0;
        for (int r = 0; r < s.length(); r++){
            while (map.contains(s.charAt(r))) {
                map.remove(s.charAt(l));
                l++;
            }
            longest = Math.max(longest, r - l + 1);
            map.add(s.charAt(r));
        }
        return longest;
    }
}
