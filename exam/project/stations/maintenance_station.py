from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.stations.base_station import BaseStation


class MaintenanceStation(BaseStation):
    INITIAL_CAPACITY = 3
    SALARY_INCREASE = 3000.0

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)

    def _salary_increase_amount(self):
        return self.SALARY_INCREASE

    def update_salaries(self, min_value: float):
        for a in self.astronauts:
            if isinstance(a, EngineerAstronaut) and a.salary <= min_value:
                a.salary += self._salary_increase_amount()