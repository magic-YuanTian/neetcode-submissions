from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:
            return ""

        target_list = self.store[key]

        left, right = 0, len(target_list) - 1

        while left <= right:
            mid = (left + right) // 2

            t = target_list[mid][0]

            if t == timestamp:
                return target_list[mid][1]

            if t > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        if right < 0:
            return ""
            
        return target_list[right][1]

