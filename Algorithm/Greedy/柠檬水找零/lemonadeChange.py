class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        Fnum = 0 #记录五块钱的数量
        Tnum = 0 #记录十块钱的数量
        for b in bills:
            if b is 5:
                Fnum += 1
            elif b is 10:
                Tnum += 1
                Fnum -= 1
                if Fnum < 0:
                    return False
            else:
                if Tnum and Fnum:
                    Tnum -= 1
                    Fnum -= 1
                elif Fnum:
                    Fnum -= 3
                    if Fnum <0:
                        return False
                else:
                    return False
        
        return True
