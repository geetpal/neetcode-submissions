class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        stack = []
        res = [0] * n
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append((t, i))
        return res




        # n = len(temperatures)
        # res = [0] * n
        # stack = []

        # for i, t in enumerate(temperatures):
        #     while stack and t > stack[-1][0]:
        #         stackT, stackInd = stack.pop()
        #         res[stackInd] = i - stackInd
        #     stack.append((t, i))
        # return res
            
        