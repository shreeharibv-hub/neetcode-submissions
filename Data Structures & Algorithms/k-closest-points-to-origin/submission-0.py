class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        data={}
        for point in points:
            x1=point[0]
            y1=point[1]
            x2=y2=0

            val=math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            if val in data:
                data[val].append(point)
            else:
                data[val] = [point]
                        

        data=sorted(data.items())

        for distance, point_list in data:
            for point in point_list:
                ans.append(point)

                if len(ans) == k:
                    return ans

        return ans