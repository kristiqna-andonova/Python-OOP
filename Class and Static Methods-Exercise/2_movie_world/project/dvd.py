import calendar


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, dvd_id: int, name: str, date: str, age_restriction: int):
        day, month, year = [int(x) for x in date.split(".")]
        return cls(name, dvd_id, year, calendar.month_name[month], age_restriction)

    def __repr__(self):
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction"
                f" {self.age_restriction}. Status: {'not rented' if not self.is_rented else 'rented'}")