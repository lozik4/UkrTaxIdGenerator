import random
from datetime import datetime, date


class TaxIdGenerator:
    """
    A class to generate INN (Individual's Taxpayer Identification Number).
    """

    def __init__(self, birthday: str = '1990-06-21', gender: int = None):
        """
        The constructor for InnGenerator class.

        :param birthday: (str) Date of Birth in 'YYYY-MM-DD' format. Default is '1990-06-21'.
        :param gender: (int) Gender, where 0 is Female and 1 is Male. Default is None which selects randomly.
        """
        if gender not in (0, 1, None):
            raise ValueError("Gender value must be 0 for Female, or 1 for Male.")
        self.birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
        self.gender = gender if gender is not None else random.randint(0, 1)

    def __select_gender(self) -> int:
        """Choose an even number for Female and odd number for Male."""
        return random.choice(range(self.gender, 10, 2))

    @staticmethod
    def __select_people_number() -> int:
        """Choose a random number between 100 and 999 (inclusive)."""
        return random.randint(100, 999)

    def __calculate_day_count(self) -> int:
        """Calculate the day count from reference date '31 December 1899'."""
        ref_date = date(1899, 12, 31)
        return (self.birthday - ref_date).days

    @staticmethod
    def __calculate_check_sum(val: str) -> int:
        """Calculate checksum using INN calculation method."""
        weights = [-1, 5, 7, 9, 4, 6, 10, 5, 7]
        checksum = sum(int(v) * w for v, w in zip(val, weights))

        return checksum % 11 % 10

    def get_tax_id(self) -> int:
        """Generate INN using day count, selected people number, gender, and checksum."""

        day_count = self.__calculate_day_count()
        people_num = self.__select_people_number()
        gender = self.__select_gender()

        inn_without_checksum = f"{day_count}{people_num}{gender}"
        checksum = self.__calculate_check_sum(inn_without_checksum)

        return int(f"{inn_without_checksum}{checksum}")


if __name__ == '__main__':
    tax_id_gen = TaxIdGenerator('1995-06-22', 0)
    print(tax_id_gen.get_tax_id())
