class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        for (int i = 0; i < s.length(); i ++){
            String c = s.substring(i, i+1);
            Integer count = map.get(c);
            if (count == null) {
                map.put(c, 1);
            }
            else {
                map.put(c, count + 1);
            }
        }

        for (int j = 0; j < t.length(); j ++){
            String c = t.substring(j,j+1);
            Integer count = map.get(c);
            if (count == null) {
                return false;
            } else { 
                count -= 1;
                if (count < 0) {
                    return false;
                }
                map.put(c, count);
            }
        }
        int maxValue = Collections.max(map.values());
        if (maxValue > 0) {
            return false;
        }
        return true;
    }
}
