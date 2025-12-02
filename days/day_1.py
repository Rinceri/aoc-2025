from fetcher.fetcher import day_input

def parse_input(raw_input: str) -> list[int]:
    out = []
    for raw_str in raw_input.split():
        sign = -1 if raw_str[0] == "L" else 1
        num = int(raw_str[1:])
        out.append(sign*num)

    return out

class Safe:
    def __init__(self, current: int = 50, start: int = 0, end: int = 99):
        self.current = current
        self.start = start
        self.end = end

        # number of times reached zero
        self.zeros = 0
        self.passing_zeros = 0

    def two_digit_rotation(self, raw_rotation: int, old_value: int) -> int:
        """
        Gets new current pointer after a rotation with last 2 digits of the actual rotation

        For example, if the old pointer was at 20 and raw rotation is -120, this will do a
        rotation of -20, returning 0 
        """
        # basically just gets remainder (not modulus) from division by 100, and adds to old value
        return (old_value + ((abs(raw_rotation) % 100) * (1 if raw_rotation >=0 else -1)))
    
    def process_input(self, rotations: list[int]):
        """
        Takes a list of integers and rotates the safe dial accordingly
        
        Stores number of times it ends at 0 after a rotation
        """
        for rotation in rotations:
            old_value = self.current
            new_current = self.current + rotation
            # performs modulus, where the "number line" is a ring
            # and since we have 100 digits, mod by 100
            self.current = new_current % 100

            first_calc = self.two_digit_rotation(rotation, old_value)

            # if old value is 0, then a negative rotation shouldn't trigger this
            # if two digit rotation causes a negative/>100 value, this means it passed zero
            # if it is 100, then it means current is 0, and will get triggered further below
            if (old_value != 0) and ((first_calc < 0) or (first_calc > 100)):
                self.passing_zeros += 1
            
            # passes zero after every 100
            if (abs(rotation) > 100):
                self.passing_zeros += abs(rotation) // 100

            if self.current == 0:
                self.zeros += 1
                self.passing_zeros += 1

    def get_zeros(self) -> int:
        return self.zeros
    
    def get_passing_zeros(self) -> int:
        return self.passing_zeros
    

def main():
    rotations = parse_input(day_input)

    safe = Safe()

    safe.process_input(rotations)
    
    print(f"Landed on zero: {safe.get_zeros()} times")
    print(f"Passed zero {safe.get_passing_zeros()} times")

main()