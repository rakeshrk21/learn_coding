class Solution:
    def findWinners(self, matches):
        winners = set() 
        lost = dict()
        lostOneTime = []

        for a in matches:
            winners.add(a[0])
            if a[1] in lost:
                lost[a[1]] += 1
            else:
                lost[a[1]]= 1
        
        for key in lost:
            if key in winners:
                winners.remove(key)
            if lost[key] < 2:
                lostOneTime.append(key)
                            
        winners = sorted(list(winners))
        lostOneTime = sorted(list(lostOneTime)) 

        return [ winners, lostOneTime]
    

if __name__ == '__main__':
    solution().findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])