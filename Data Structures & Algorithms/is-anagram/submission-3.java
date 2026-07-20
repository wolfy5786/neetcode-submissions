class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> first = new  HashMap<>();
        for (char c: s.toCharArray())
        {
            first.put(c,first.getOrDefault(c,0) + 1);
        }
        for (char c : t.toCharArray())
        {
            if(first.containsKey(c))
            {
                if(first.get(c) >0)
                {
                    first.put(c,first.get(c) - 1);
                }
                else{
                    return false;
                }
            }
            else{
                return false;
            }
        }
        for (Map.Entry<Character, Integer> entry : first.entrySet())
        {
            if(entry.getValue()!=0)
            {
                return false;
            }
        }
        return true;
    }
}
