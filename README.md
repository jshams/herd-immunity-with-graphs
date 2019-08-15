# Herd Immunity

## What is the project?
My final goal is to create a simulation of a virus through a network of people. This will work by creating a population using a network graph and giving the virus to a number of people. Then I will have people in my population interact with people they know and possibly spread the virus. 

This program uses my custom [Graph class](https://github.com/jshams/CS-2.2-Advanced-Recursion-and-Graphs/) for storing the population. 

## How can graph theory concepts be applied?
- I can find the most vulnerable person in the population (using dynamic programming)

- I can find the most dangerours persom in the population

- I can find out if one person has another person in their extended network that is infected DFS

- I can find out the diameter of the graph to see how connected people are.
---

## Classes:

### Person:
The person class sotres data about the person.

Attributes:
- `id` - int -Used to identify a person object
- `is_vaccinated` - boolean - decares whether a person is vaccinated or not.
- `is_infected` - boolean - declares whether a person is infected of not.
- `is_alive` - boolean - declares whether a person is alive or not.


### Virus:
The virus class stores data about the virus.

Attributes:
- `virus_name` - string - the name of the virus
- `mortality rate` - float - how dealy the virus is. This is the percentage (0.0-1.0) of infected people that will die from infection. The opposite of survival rate.  
- `Transmission` - float - The likelihood (percentage 0-1) an uninfected person will become infected after interacting with another infected person.


### Simulation:
Creates a simulation of the virus using a graph class to create the population.

Attributes:
- `population_graph` - Graph - Stores the population in a graph.
- `virus_name` - string - the name of the virus
- `population_size` - int - the size of the population
- `vacc_percentage` - float - percentage (0.0-1.0) of people that initially get vaccinated.
- `mortality_rate` - float - how dealy the virus is. This is the percentage (0.0-1.0) 
- `transmission` 
- `initial_infected` 
- `total_infected` 
- `current_infected` 
- `total_dead` 
- `_create_population`
- `_create_population_connections`