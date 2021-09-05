class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))

        res = s
        new_res = res
        for i in range(1, len(s)):
            new_res = new_res[1:] + new_res[0]
            if new_res < res:
                res = new_res
        return res
