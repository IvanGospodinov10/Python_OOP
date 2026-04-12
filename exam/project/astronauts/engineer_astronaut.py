from project.astronauts.base_astronaut import BaseAstronaut


class EngineerAstronaut(BaseAstronaut):
    INITIAL_STAMINA = 80

    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, "EngineerAstronaut",self.INITIAL_STAMINA)

    def train(self):
        stamina_increase = 5
        new_stamina = self.stamina + stamina_increase

        if new_stamina > 100:
            new_stamina = 100
        self.stamina = new_stamina
