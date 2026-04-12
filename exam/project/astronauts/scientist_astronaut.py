from project.astronauts.base_astronaut import BaseAstronaut


class ScientistAstronaut(BaseAstronaut):
    INITIAL_STAMINA = 70

    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, "ScientistAstronaut", self.INITIAL_STAMINA)

    def train(self):
        stamina_increase = 3
        new_stamina = self.stamina + stamina_increase

        if new_stamina > 100:
            new_stamina = 100
        self.stamina = new_stamina