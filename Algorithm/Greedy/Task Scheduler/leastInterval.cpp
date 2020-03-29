class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int>counter(26,0);
        for (char t:tasks)
        {
            ++counter[t-'A'];
        }
        int m = *max_element(counter.begin(),counter.end());
        int p = count(counter.begin(),counter.end(),m);
        return max((m-1)*(n+1)+p,int(tasks.size()));
    }
};
