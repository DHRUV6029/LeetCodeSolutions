class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
        int len = bloomDay.length;
        if(m*k > len) return -1;
        int right = 0, left = Integer.MAX_VALUE;
        
        for(int day: bloomDay)
        {
            right = Math.max(right, day);
            left = Math.min(left, day);
        }
        
        int mid = 0;
        while(left < right)
        {
            mid = left + (right - left)/2;
            if(!canBloom(mid, bloomDay, m, k))
                left = mid + 1;
            else
                right = mid;
        }
        
        return left;
    }
    
    public boolean canBloom(int mid, int[] nums, int m, int k)
    {
        long ans = 0;
        long continous = 0;
        for(int n: nums)
        {
            if(n <= mid)
                continous++; 
            else
                continous = 0;
            if(continous == k)
            {
                ans++;
                continous = 0;
            }   
            if(ans == m)
                return true;
        }
        return false;
    }
}