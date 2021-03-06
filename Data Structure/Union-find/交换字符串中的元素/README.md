**题目链接**:https://leetcode-cn.com/problems/smallest-string-with-swaps/  

**题目描述**:  
```
给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。

你可以 任意多次交换 在 pairs 中任意一对索引处的字符。

返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。
```

**示例**:
```
输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
输出："abcd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[0] 和 s[2], s = "acbd"
交换 s[1] 和 s[2], s = "abcd"
```

**解题思路**:  
如果几个字符串是连通的，那么说明，他们的位置可以相互调换，那就可以把字典序小的放在他们位置的前面即可。  
1.合并  
2.分组，把用一个集合的元素分好组，当时遇到的问题是不知道怎么样才能把同一个集合分成同一个组，其实用字典[root]=element就好了。
3.对同组元素和索引排序
4.把字典序小的放在前面
