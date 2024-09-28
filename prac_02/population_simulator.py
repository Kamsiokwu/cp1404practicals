import random

def gopher_population_simulator():
    global gophers_died
    population = 1000
    print("Welcome to the Gopher Population Program !!")
    print(f"Starting population: {population}\n")

    for year in range(1, 11):
        # Calculate number of gophers born (10% upto 20%)
        birth_rate = random.uniform(0.10, 0.20)
        gophers_born = int(population * birth_rate)
        if gophers_born > 0:

            death_rate = random.uniform(0.05, 0.25)
            gophers_died = int(population * death_rate)
            population += gophers_born - gophers_died
        else:
            print("No gophers born")

        # Display results for the year
        print(f"Year {year}")
        print(f"\n{gophers_born} gophers were born. {gophers_died} died.")
        print(f"Population: {population}\n")

# Run the simulation
gopher_population_simulator()
