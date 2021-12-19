from Lecture_7_ui.Person import Person


class Coach(Person):
    def __init__(self, name, person_id, birth_year, seniority, rule):
        super().__init__(name, person_id, birth_year)
        self.seniority = seniority
        self.rule = rule

    def __str__(self):
        back = super().__str__()
        return f"{back}, {self.seniority}, {self.rule}"

    def print_me(self):
        super().print_me()
        print(f"seniority: {self.seniority}")
        print(f"rule: {self.rule}")
