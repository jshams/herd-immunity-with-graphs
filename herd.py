from graph import ADTGraph
from random import random, randint, choice


class Person():
    def __init__(self, _id, is_vaccinated: bool, is_infected=False):
        self.id = _id
        self.is_vaccinated = is_vaccinated
        self.is_infected = is_infected
        self.is_alive = True

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def died(self):
        self.is_alive = False

    def did_survive_infection(self, mortality_rate):
        pass


class Virus():
    def __init__(self, virus_name, mortality_rate, transmission):
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.transmission = transmission


class Simulation(object):

    def __init__(self, virus_name: str, population_size: int, vacc_percentage: float, mortality_rate: float, transmission: float, initial_infected=1):
        self.population_graph = ADTGraph()
        self.population_graph.digraph = False
        self.virus_name = virus_name
        self.population_size = population_size
        self.vacc_percentage = vacc_percentage
        self.mortality_rate = mortality_rate
        self.transmission = transmission
        self.initial_infected = initial_infected
        self.total_infected = initial_infected
        self.current_infected = initial_infected
        self.total_dead = 0
        self._create_population()
        self._create_population_connections()

    def _create_population(self):
        '''creates a population with population_size(int) people
        Will create initial_infected(int) people infected
        Will also create about vacc_percentage(float 0-1) vaccinated people'''
        for i in range(self.population_size):
            if i < self.initial_infected:
                # create an infected person
                infected_person = Person(i, False, True)
                self.population_graph.add_vertex(infected_person)
            else:  # create a healthy person
                # if random float from 0 - 1 is less than the vacc pct
                if random() < self.vacc_percentage:
                    # create a healthy vaccinated person
                    healthy_vaccinated_person = Person(i, True, False)
                    self.population_graph.add_vertex(healthy_vaccinated_person)
                else:
                    # create a healthy unvaccinated person
                    healthy_person = Person(i, False, False)
                    self.population_graph.add_vertex(healthy_person)

    def _create_population_connections(self):
        '''Create random edges between already created vertices'''
        lst_of_people = [person for person in self.population_graph]
        from math import log
        avg_connections = int(log(10 * self.population_size, 10) ** 2)
        for _ in range(self.population_size * avg_connections):
            random_person = choice(lst_of_people)
            other_random_person = choice(lst_of_people)
            while other_random_person == random_person:
                other_random_person = choice(lst_of_people)
            self.population_graph.add_edge(random_person, other_random_person)

    def _simulation_should_continue(self):
        '''Returns a boolean indicating whether or not to continue simulation'''
        if self.population_size == self.total_dead:
            print('Everybody died')
            return False
        elif self.current_infected == 0:
            print("The disease stopped spreading")
            return False
        else:
            return True

    def run(self):
        while self._simulation_should_continue():
            self.time_step()

    def time_step(self):
        '''Every day we have a new timestep.
        People are less likely to interact with others if they are sick.
        If a vaccinated person interacts with someone who is not vaccinated
        they can try to convince them to get vaccinated.
        If a sick person interracts with a healthy person
        '''
        pass

    def random_person(self, person):
        '''Given a person find another random person they should interact with
        It isn't exactly random though
        There is a 20% chance that person is not in their direct network
        On the 80% that they do know the person
        There is a 75% chance that person is in their first network
        On the 25% chance they are in their second network we recursively call this method
        So then there is again a 20% chance random, 60% they directly know the person and
        20% in their extended network.'''
        pass

    def interaction(self, sick_person, random_person):
        pass

    def _infect_newly_infected(self):
        pass

    def predict_danger(self, person):
        # if a person is healthy, vaccinated, or dead they are not harmful
        if not person.is_infected or person.is_vaccinated or not person.is_alive:
            return 0
        danger = 0
        network_levels = self.population_graph.find_network_levels(person)
        for level, others in network_levels.items():
            if level == 0:
                continue
            healthy_unvaccinated_friends = 0
            for person in others:
                if not person.is_infected and not person.is_vaccinated and person.is_alive:
                    healthy_unvaccinated_friends += 1
            danger += (healthy_unvaccinated_friends /
                       len(others)) * 0.2 ** (level - 1)
        return danger

    def find_most_dangerous(self):
        most_dangerous_person = None
        max_danger = 0
        for person in self.population_graph:
            danger = self.predict_danger(person)
            if danger > max_danger or most_dangerous_person is None:
                max_danger = danger
                most_dangerous_person = person
        print('max-danger', max_danger)
        return most_dangerous_person

    def predict_vulnerability(self, person: Person):
        # if a person is infected, vaccinated, or dead they are not vulnerable
        if person.is_infected or person.is_vaccinated or not person.is_alive:
            return 0
        vulnerability = 0
        network_levels = self.population_graph.find_network_levels(person)
        for level, others in network_levels.items():
            if level == 0:
                continue
            sick_friends = len(
                [sick_person for sick_person in others if sick_person.is_infected])
            vulnerability += (sick_friends / len(others)) * 0.2 ** (level - 1)
        return vulnerability

    def find_most_vulnerable(self):
        most_vulnerable_person = None
        max_vulnerability = 0
        for person in self.population_graph:
            vulnerability = self.predict_vulnerability(person)
            if vulnerability > max_vulnerability or most_vulnerable_person is None:
                max_vulnerability = vulnerability
                most_vulnerable_person = person
        print('max-vulnerability', max_vulnerability)
        return most_vulnerable_person


if __name__ == '__main__':
    sim = Simulation("Ebola", 100, 0.2,  0.5, 0.3, 10)
    dia = sim.population_graph.diameter()
