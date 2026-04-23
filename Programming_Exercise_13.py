import sqlite3
import random
import matplotlib.pyplot as plt


def create_database():
    # connect to database
    conn = sqlite3.connect("population_TS.db")   # change TS to your initials
    cur = conn.cursor()

    # create table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)

    # delete old data so it does not duplicate
    cur.execute("DELETE FROM population")

    # 10 Florida cities for year 2025
    cities = [
        ("Jacksonville", 2025, 1000000),
        ("Miami", 2025, 470000),
        ("Tampa", 2025, 415000),
        ("Orlando", 2025, 330000),
        ("St. Petersburg", 2025, 270000),
        ("Hialeah", 2025, 225000),
        ("Tallahassee", 2025, 205000),
        ("Fort Lauderdale", 2025, 185000),
        ("Cape Coral", 2025, 245000),
        ("Gainesville", 2025, 150000)
    ]

    # insert starting data
    cur.executemany("INSERT INTO population VALUES (?, ?, ?)", cities)

    conn.commit()
    conn.close()


def simulate_population():
    # connect to database
    conn = sqlite3.connect("population_TS.db")   # change TS to your initials
    cur = conn.cursor()

    # get the 2025 data
    cur.execute("SELECT city, population FROM population WHERE year = 2025")
    rows = cur.fetchall()

    # simulate next 20 years
    for row in rows:
        city = row[0]
        pop = row[1]

        for year in range(2026, 2046):
            rate = random.uniform(-0.02, 0.05)   # between -2% and 5%
            pop = int(pop * (1 + rate))

            cur.execute("INSERT INTO population VALUES (?, ?, ?)", (city, year, pop))

    conn.commit()
    conn.close()


def show_graph():
    # connect to database
    conn = sqlite3.connect("population_TS.db")   # change TS to your initials
    cur = conn.cursor()

    # list city options
    city_list = [
        "Jacksonville",
        "Miami",
        "Tampa",
        "Orlando",
        "St. Petersburg",
        "Hialeah",
        "Tallahassee",
        "Fort Lauderdale",
        "Cape Coral",
        "Gainesville"
    ]

    print("Choose a city:")
    for i in range(len(city_list)):
        print(i + 1, "-", city_list[i])

    choice = int(input("Enter the number of the city: "))
    city_name = city_list[choice - 1]

    # get data for selected city
    cur.execute("SELECT year, population FROM population WHERE city = ? ORDER BY year", (city_name,))
    data = cur.fetchall()

    years = []
    populations = []

    for row in data:
        years.append(row[0])
        populations.append(row[1])

    conn.close()

    # make graph
    plt.plot(years, populations, marker="o")
    plt.title("Population Change for " + city_name)
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.show()


def main():
    create_database()
    simulate_population()
    show_graph()


main()