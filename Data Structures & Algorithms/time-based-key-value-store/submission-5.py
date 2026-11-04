from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""

        values = self.hmap[key]

        idx = bisect.bisect_right(
            values, timestamp, key=lambda x: x[0]
        ) - 1

        if idx < 0:
            return ""

        return values[idx][1]