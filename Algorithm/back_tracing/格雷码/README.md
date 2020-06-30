**题目链接** :
https://leetcode-cn.com/problems/gray-code/

**解题思路**:
![Image](https://github.com/WeifaGan/MyLeetCode/blob/master/Image/graycode.png)

1.从图中可以看到每次添加顺序都是0110，例如，从n=2到3，相对于n=2时候，添加顺序就是0110 0110...，所以便可以总结规律。
2.n=1时候，格雷码是[0,1]，[0,1]经过一番操作后得到n=2的格雷码[0 1 3 2]。
