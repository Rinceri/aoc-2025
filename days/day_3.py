from fetcher.fetcher import day_input

class OrderedBatteries:
    def __init__(self, all_batteries: str, output_batteries: int):
        self.batteries = [int(battery) for battery in all_batteries][::-1]

        self.order = []
        self.output_batteries = output_batteries

    def get_joltage(self) -> int:
        for battery in self.batteries:
            if len(self.order) < self.output_batteries:
                # list hasn't fully populated yet
                self.order = [battery] + self.order
            else:
                # recursively replace batteries if higher value
                self.replace_battery(0, battery)

        return self.get_int_order()
    
    def get_int_order(self) -> int:
        return int(''.join(map(str, self.order)))

    def replace_first_battery(self, battery: int):
        old_first = self.order[0]
        self.order[0] = battery

        return old_first
        
    def replace_last_battery(self, previous_battery: int):
        if previous_battery > self.order[-1]:
            self.order[-1] = previous_battery

    def replace_battery(self, battery_at_order: int, curr_battery: int):
        if battery_at_order == self.output_batteries:
            self.replace_last_battery(curr_battery)
            return

        if curr_battery >= self.order[battery_at_order]:
            old_battery = self.order[battery_at_order]
            self.order[battery_at_order] = curr_battery
            self.replace_battery(battery_at_order + 1, curr_battery = old_battery)
        

def main():
    running_total = 0

    for i in day_input.split("\n"):
        ordered_batteries = OrderedBatteries(i, 12)
        running_total += ordered_batteries.get_joltage()

    print("Total joltage: ", running_total)

main()