"""
TFDP Democracy Analyzer

Code in Place 2026 Final Project

The Future of Democracy Project (TFDP)
"""

import os
import json


# Display the main menu.
def print_menu():

    print()
    print("TFDP DEMOCRACY ANALYZER")
    print("=======================")
    print()
    print("1 - New Analysis")
    print("2 - View History")
    print("3 - Compare Countries")
    print("4 - Democracy Dashboard")
    print("5 - World Ranking")
    print("6 - Database Statistics")
    print("7 - Exit")
    print()


# Get indicator value from user.
def get_indicator(name):

    while True:

        try:

            value = float(input(f"{name} (0-100): "))

            if 0 <= value <= 100:
                return value

            print("Value must be between 0 and 100.")

        except ValueError:

            print("Please enter a valid number.")


# Calculate TFDP score.
def calculate_tfdp_score(
    electoral_integrity,
    civil_liberties,
    transparency,
    education,
    economy
):

    score = (
        electoral_integrity * 0.30 +
        civil_liberties * 0.25 +
        transparency * 0.20 +
        education * 0.15 +
        economy * 0.10
    )

    return round(score, 2)


# Classify country.
def classify_country(score):

    if score >= 80:
        return "Strong Democracy"

    elif score >= 60:
        return "Stable Democracy"

    elif score >= 40:
        return "Democracy at Risk"

    elif score >= 20:
        return "Fragile Democracy"

    else:
        return "Emerging Authoritarianism"


# Generate TFDP assessment.
def democracy_assessment(score):

    if score >= 80:
        return (
            "This country demonstrates strong democratic "
            "institutions and low risk of democratic erosion."
        )

    elif score >= 60:
        return (
            "This country maintains democratic stability "
            "but should continue strengthening institutions."
        )

    elif score >= 40:
        return (
            "This country shows warning signs of democratic "
            "fragility and requires institutional attention."
        )

    elif score >= 20:
        return (
            "This country presents significant democratic "
            "weaknesses and elevated erosion risks."
        )

    else:
        return (
            "This country demonstrates severe democratic "
            "decline and authoritarian tendencies."
        )


# Start a new analysis.
def new_analysis():

    print()
    print("NEW DEMOCRACY ANALYSIS")
    print("----------------------")

    country = input("Country Name: ")

    electoral_integrity = get_indicator("Electoral Integrity")
    civil_liberties = get_indicator("Civil Liberties")
    transparency = get_indicator("Government Transparency")
    education = get_indicator("Education Index")
    economy = get_indicator("Economic Stability")

    score = calculate_tfdp_score(
        electoral_integrity,
        civil_liberties,
        transparency,
        education,
        economy
    )

    classification = classify_country(score)

    print()
    print("FINAL REPORT")
    print("----------------------")

    print(f"Country: {country}")
    print(f"TFDP Score: {score}")
    print(f"Classification: {classification}")

    print()
    print("TFDP ASSESSMENT")
    print("----------------------")
    print(democracy_assessment(score))

    save_report(
        country,
        electoral_integrity,
        civil_liberties,
        transparency,
        education,
        economy,
        score,
        classification
    )


# Save report.
def save_report(
    country,
    electoral_integrity,
    civil_liberties,
    transparency,
    education,
    economy,
    score,
    classification
):

    current_folder = os.path.dirname(os.path.abspath(__file__))

    txt_path = os.path.join(
        current_folder,
        "tfdp_reports.txt"
    )

    database_path = os.path.join(
        current_folder,
        "tfdp_database.json"
    )

    country_data = {
        "country": country,
        "electoral_integrity": electoral_integrity,
        "civil_liberties": civil_liberties,
        "transparency": transparency,
        "education": education,
        "economy": economy,
        "score": score,
        "classification": classification
    }

    with open(
        txt_path,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(f"Country: {country}\n")
        file.write(f"Score: {score}\n")
        file.write(
            f"Classification: {classification}\n"
        )
        file.write("-" * 40 + "\n")

    try:

        with open(
            database_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        data = []

    updated = False

    for index in range(len(data)):

        if (
            data[index]["country"].lower()
            ==
            country.lower()
        ):

            data[index] = country_data
            updated = True
            break

    if not updated:

        data.append(country_data)

    with open(
        database_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    print()
    print("Analysis saved successfully.")


# View history.
def show_history():

    current_folder = os.path.dirname(
        os.path.abspath(__file__)
    )

    file_path = os.path.join(
        current_folder,
        "tfdp_reports.txt"
    )

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            print()
            print("ANALYSIS HISTORY")
            print("================")
            print()

            print(file.read())

    except FileNotFoundError:

        print("No history found.")


# Find country.
def find_country(country_name):

    current_folder = os.path.dirname(
        os.path.abspath(__file__)
    )

    database_path = os.path.join(
        current_folder,
        "tfdp_database.json"
    )

    try:

        with open(
            database_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        return None

    for country in data:

        if (
            country["country"].lower()
            ==
            country_name.lower()
        ):

            return country

    return None


# Compare countries.
def compare_saved_countries():

    print()
    print("COUNTRY COMPARISON")
    print("------------------")

    country1 = input("Country 1: ")
    country2 = input("Country 2: ")

    data1 = find_country(country1)
    data2 = find_country(country2)

    if data1 is None:
        print("Country not found.")
        return

    if data2 is None:
        print("Country not found.")
        return

    difference = abs(
        data1["score"] - data2["score"]
    )

    print()
    print("COMPARISON REPORT")
    print("------------------")

    print(
        f"{country1}: {data1['score']}"
    )

    print(
        f"{country2}: {data2['score']}"
    )

    print(
        f"Difference: {difference:.2f}"
    )


# Print bar chart.
def print_bar(name, value):

    bar = "█" * int(value / 5)

    print(
        f"{name:<22} "
        f"{bar} "
        f"({value})"
    )


# Country dashboard.
def democracy_dashboard():

    print()
    print("DEMOCRACY DASHBOARD")
    print("===================")

    country_name = input(
        "Country Name: "
    )

    country = find_country(country_name)

    if country is None:

        print("Country not found.")
        return

    print()
    print(
        f"Country: {country['country']}"
    )

    print(
        f"TFDP Score: {country['score']}"
    )

    print(
        f"Classification: "
        f"{country['classification']}"
    )

    print()

    print_bar(
        "Electoral Integrity",
        country["electoral_integrity"]
    )

    print_bar(
        "Civil Liberties",
        country["civil_liberties"]
    )

    print_bar(
        "Transparency",
        country["transparency"]
    )

    print_bar(
        "Education",
        country["education"]
    )

    print_bar(
        "Economy",
        country["economy"]
    )


# World ranking.
def show_world_ranking():

    current_folder = os.path.dirname(
        os.path.abspath(__file__)
    )

    database_path = os.path.join(
        current_folder,
        "tfdp_database.json"
    )

    try:

        with open(
            database_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        print("Database not found.")
        return

    ranking = sorted(
        data,
        key=lambda item: item["score"],
        reverse=True
    )

    print()
    print("WORLD RANKING")
    print("=============")

    for position, country in enumerate(
        ranking,
        start=1
    ):

        print(
            f"{position}. "
            f"{country['country']} "
            f"- "
            f"{country['score']}"
        )


# Database statistics.
def database_statistics():

    current_folder = os.path.dirname(
        os.path.abspath(__file__)
    )

    database_path = os.path.join(
        current_folder,
        "tfdp_database.json"
    )

    try:

        with open(
            database_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        print("Database not found.")
        return

    if len(data) == 0:

        print("No data available.")
        return

    total_score = 0

    highest = data[0]
    lowest = data[0]

    for country in data:

        total_score += country["score"]

        if (
            country["score"]
            >
            highest["score"]
        ):

            highest = country

        if (
            country["score"]
            <
            lowest["score"]
        ):

            lowest = country

    average = total_score / len(data)

    print()
    print("DATABASE STATISTICS")
    print("===================")

    print(
        f"Countries analyzed: {len(data)}"
    )

    print(
        f"Average score: {average:.2f}"
    )

    print()

    print(
        f"Highest score: "
        f"{highest['country']} "
        f"({highest['score']})"
    )

    print(
        f"Lowest score: "
        f"{lowest['country']} "
        f"({lowest['score']})"
    )


# Main function.
def main():

    while True:

        print_menu()

        option = input(
            "Choose an option: "
        )

        if option == "1":

            new_analysis()

        elif option == "2":

            show_history()

        elif option == "3":

            compare_saved_countries()

        elif option == "4":

            democracy_dashboard()

        elif option == "5":

            show_world_ranking()

        elif option == "6":

            database_statistics()

        elif option == "7":

            print("Goodbye!")
            break

        else:

            print(
                "Invalid option."
            )


if __name__ == "__main__":
    main()