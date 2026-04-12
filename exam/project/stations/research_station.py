from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation



class ResearchStation(BaseStation):
    SALARY_INCREASE = 5000.0
    INITIAL_CAPACITY = 5

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)

    def _salary_increase_amount(self):
        return self.SALARY_INCREASE

    def update_salaries(self, min_value: float):
        for a in self.astronauts:
            if isinstance(a, ScientistAstronaut) and a.salary <= min_value:
                a.salary += self._salary_increase_amount()
