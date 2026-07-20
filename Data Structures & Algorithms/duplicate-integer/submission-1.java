class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> hm = new HashMap<>();
        for(int num : nums)
        {
            if(!hm.containsKey(num))
            {
                hm.put(num,num);
            }
            else{
                return true;
            }
        }
        return false;
    }
}