class Solution:
    def findPairsWithGivenSum(
        self, target: int, head: Optional["Node"]
    ) -> List[List[int]]:
        # code here
        l1 = []
        hash_map = {}
        current = head
        while current:
            a = current.data
            b = target - a
            if b in hash_map:
                l1.insert(0, (b, a))
            else:
                hash_map[a] = 1
            current = current.next
        return l1
