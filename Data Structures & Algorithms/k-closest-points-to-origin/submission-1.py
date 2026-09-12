class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Map point to their euclidian distance
        coorMap = {}
        for x,y in points:
            coorMap[(x,y)] = self.euclideanDistance([x,y], [0,0])
        coorMap = sorted(coorMap.items(), reverse=True, key=lambda item: item[1])
        res = [list(key[0]) for key in coorMap]
        while len(res) > k:
            res.remove(res[0])
        return res[0:]

    def euclideanDistance(self, coordinate1: list[int], coordinate2: list[int]) -> float:
        x = (coordinate1[0] - coordinate2[0])
        y = (coordinate1[1] - coordinate2[1])
        res = math.sqrt((x*x) + (y*y))
        return res