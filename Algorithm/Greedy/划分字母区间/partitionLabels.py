class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        max_index={item:index for index,item in enumerate(S)}
        lst = []
        start = 0
        end = 0
        for cur_index,item in enumerate(S):
            end = max(cur_index,end)
            if end<max_index[item]:end = max_index[item]

            if end==cur_index:
                lst.append(end-start+1)
                start = end+1
            

        return lst
