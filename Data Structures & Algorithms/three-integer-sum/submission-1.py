class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, p, z, res = [], [], [], []

        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)
            
        N = set(n)
        P = set(p)

        if len(z) >= 3:
            res.append([0,0,0])
        
        if z:
            for num in N:
                if -1*num in P:
                    if [num, 0, -1*num] not in res:
                        res.append([num, 0, -1*num])
        
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                if -1 * (n[i] + n[j]) in P:
                    if sorted([n[i],n[j],-1 * (n[i] + n[j])]) not in res:
                        res.append(sorted([n[i],n[j],-1 * (n[i] + n[j])]))

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                if -1 * (p[i] + p[j]) in N:
                    if sorted([p[i],p[j],-1 * (p[i] + p[j])]) not in res:
                        res.append(sorted([p[i],p[j],-1 * (p[i] + p[j])]))
        
        return res
        

