from abc import ABC, abstractmethod

from project.astronauts.base_astronaut import BaseAstronaut


class BaseStation(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.astronauts: list[BaseAstronaut] = []
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not all(ch.isalnum() or ch == "-" for ch in value):
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        self.__name = value
        
    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("A station cannot have a negative capacity!")
        self.__capacity = value

    def calculate_total_salaries(self):
        total_salary = sum(a.salary for a in self.astronauts)
        return f"{total_salary:.2f}"

    def status(self):
        if not self.astronauts:
            astronauts_info = "N/A"
        else:
            astronauts_info = " #".join(sorted(a.id_number for a in self.astronauts))

        total_salaries = self.calculate_total_salaries()

        return f"Station name: {self.name}; Astronauts: {astronauts_info}; Total salaries: {total_salaries}"

    @abstractmethod
    def _salary_increase_amount(self):
        pass

    def update_salaries(self, min_value: float):
        salary_increase_amount = self._salary_increase_amount()

        for a in self.astronauts:
            if a.salary <= min_value:
                a.salary += salary_increase_amount
