from graph import ADTGraph
from random import random, randint, choice


class Person():
    def __init__(self, _id, is_vaccinated: bool, infected=False):
        self.id = _id
        self.is_vaccinated = is_vaccinated
        self.infected = infected
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
    def __init__(self, virus_name, mortality_rate, basic_repro_num):
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num


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

        # self.population = self._create_population(self.initial_infected)

    def _create_population(self):
        '''creates a population with population_size(int) people
        Will create initial_infected(int) people infected
        Will also create about vacc_percentage(float 0-1) vaccinated people'''
        pass

    def _create_population_connections(self):
        '''Create random edges between already created vertices'''
        pass

    def _simulation_should_continue(self):
        '''Returns a boolean indicating whether or not to continue simulation'''
        pass

    def run(self):
        pass

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
