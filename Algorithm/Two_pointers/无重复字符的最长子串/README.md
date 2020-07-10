**题目链接**:
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

**解题思路**:
* 感觉突破口是要知道右指针所指的便是重复的数字！
* 用set来存放数据！可以更快判断元素是否重复，若重复了，移动左指针使得窗口不包含重复数字。
* 套用模块，不过要灵活处理
* set仅仅存放双指针范围的数据
