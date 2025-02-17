from typing import List

# 两个列表的交集
def instersection(list1: List[int or str], list2: List[int or str]) -> List[int or str]:
    return list(set(list1) & set(list2))
