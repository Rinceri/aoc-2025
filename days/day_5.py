from fetcher.fetcher import day_input


class RangePointer:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"{self.start} -> {self.end}"

    def sum_up(self):
        return self.end - self.start + 1
    
    def in_range(self, num: int):
        return num >= self.start and num <= self.end


class Ranger:
    def __init__(self):
        self.ranges: list[RangePointer] = []

    def check_against(self, num: int):
        for r in self.ranges:
            if r.in_range(num):
                return True
        
        return False
    
    def get_considered_fresh(self) -> int:
        """
        Returns number of ingredients that can be considered fresh by these ranges
        """
        total = 0
        for r in self.ranges:
            total += r.sum_up()

        return total

    def add_range(self, curr: str):
        min_max = curr.split("-")
        curr_min = int(min_max[0])
        curr_max = int(min_max[1])
        add_pt = True
        remove_elements = []
        
        for i, r in enumerate(self.ranges):
            if curr_min >= r.start:
                # curr_min is greater than this range's start
                if curr_min <= r.end:
                    # curr_min is overlapping with this range
                    if curr_max > r.end:
                        # curr_max is greater than this range's end
                        # merge ranges
                        remove_elements.append(r)
                        curr_min = r.start
                    else:
                        # curr_range falls under this range
                        # as curr_max < r.end
                        add_pt = False
                else:
                    # current range is greater than this range, move on
                    continue
            else:
                # curr_min is less than this range's start
                if curr_max < r.start:
                    # curr_max is before this range's start
                    continue
                elif curr_max >= r.end:
                    # curr_max includes this range
                    # remove this range object
                    remove_elements.append(r)
                elif curr_max >= r.start:
                    # curr range overlaps with this range
                    remove_elements.append(r)
                    curr_max = r.end

        for i in remove_elements:
            self.ranges.remove(i)

        if add_pt:
            self.ranges.append(RangePointer(curr_min, curr_max))


def main():
    split_up = day_input.split("\n\n")
    ranger = Ranger()
    fresh_ingredients = 0
    
    for range_ in split_up[0].split("\n"):
        ranger.add_range(range_)
    
    for ingredient in split_up[1].split("\n"):
        if ranger.check_against(int(ingredient)):
            fresh_ingredients += 1
    
    print(f"{fresh_ingredients} fresh ingredients based on given list")
    print(f"{ranger.get_considered_fresh()} considered fresh ingredients")


main()