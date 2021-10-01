import re
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def addOperator(term, index):
            if index == len(num):
                if eval(term) == target:
                    res.append(term)
                return
            if re.split('\+|\-|\*', term)[-1] != "0":
                addOperator(term + num[index], index + 1)
            addOperator(term + "+" + num[index], index + 1)
            addOperator(term + "-" + num[index], index + 1)
            addOperator(term + "*" + num[index], index + 1)

        addOperator(num[0], 1)
        return res
