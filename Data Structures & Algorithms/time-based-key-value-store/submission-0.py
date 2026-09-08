class TimeMap:

    def __init__(self):
        self.h_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.h_map:
            self.h_map[key] = []
        self.h_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.h_map:
            return ""
        
        # Binary search for the timestamp_preve <= timestamp
        v_list = self.h_map[key]
        l = 0
        r = len(v_list) - 1
        result = ""

        while l <= r:
            mid = l + (r - l) // 2
            if v_list[mid][0] <= timestamp:
                # search right
                l = mid + 1
                result = v_list[mid][1]
            else:
                r = mid - 1
        return result


        
