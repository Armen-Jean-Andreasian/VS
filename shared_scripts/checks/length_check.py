class LengthCheck:
    @staticmethod
    def check(iterable, desired_length: int) -> None:
        """Checks if the given iterable has the desired length, raises ValueError if not """
        if iterable.__len__() < desired_length:
            raise ValueError(f"Unable to pair {iterable.__len__()} item")
