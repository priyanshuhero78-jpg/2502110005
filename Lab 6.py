IT12 – Three Jigs Create a new Python file called lab04_jigs.py.


# Function 1: Inspect diameter and return a bin label
def inspect(dia):
    """Classifies a diameter into a bin label."""
    if dia < 10:
        return "Small"
    elif dia < 20:
        return "Medium"
    else:
        return "Large"


# Function 2: Count the labels
def tally(labels):
    """Returns a dictionary containing label counts."""
    counts = {}

    for label in labels:
        counts[label] = counts.get(label, 0) + 1

    return counts


# Function 3: Generate a formatted report
def report(shift, counts):
    """Returns a formatted shift report."""
    result = f"Shift {shift}: "

    for label, count in counts.items():
        result += f"{label} = {count}, "

    return result.rstrip(", ")


# Testing each function separately
print("Testing inspect():")
print(inspect(5))
print(inspect(15))
print(inspect(25))

print("\nTesting tally():")
labels = ["Small", "Medium", "Small", "Large", "Medium"]
counts = tally(labels)
print(counts)

print("\nTesting report():")
print(report("A", counts))
     
Testing inspect():
Small
Medium
Large

Testing tally():
{'Small': 2, 'Medium': 2, 'Large': 1}

Testing report():
Shift A: Small = 2, Medium = 2, Large = 1
IT10 – Refactor Lab 04 Open your existing lab04_autobench.py.


# Function to inspect diameter
def inspect(dia):
    """Returns the category of a given diameter."""
    if dia < 10:
        return "Small"
    elif dia < 20:
        return "Medium"
    else:
        return "Large"


# Function to count labels
def tally(labels):
    """Counts the number of each label."""
    counts = {}

    for label in labels:
        counts[label] = counts.get(label, 0) + 1

    return counts


# Function to generate report
def report(shift, counts):
    """Creates a formatted report."""
    result = f"Shift {shift}: "

    for label, count in counts.items():
        result += f"{label} = {count}, "

    return result.rstrip(", ")


# Main program
if __name__ == "__main__":

    diameters = [5, 12, 8, 25, 15, 30]

    labels = []

    for dia in diameters:
        labels.append(inspect(dia))

    counts = tally(labels)

    print(report("A", counts))
     
Shift A: Small = 2, Medium = 2, Large = 2
IT8 – The Parts Catalogue Now add a dictionary to store part codes and diameters.


# Parts catalogue
catalogue = {
    "P101": 10,
    "P102": 15,
    "P103": 20,
    "P104": 25,
    "P105": 30
}


# Function to look up a part
def lookup(catalogue, code):
    """Returns diameter or a default value."""
    return catalogue.get(code, "Unknown Part")


# Function to find scrap codes
def scrap_codes(catalogue):
    """Returns part codes outside the specified range."""
    scrap = set()

    for code, diameter in catalogue.items():
        if diameter < 10 or diameter > 25:
            scrap.add(code)

    return scrap


# Main program
if __name__ == "__main__":

    print("Parts Catalogue:")
    print(catalogue)

    print("\nPart Lookup:")
    print("P101:", lookup(catalogue, "P101"))
    print("P999:", lookup(catalogue, "P999"))

    print("\nScrap Parts:")
    print(scrap_codes(catalogue))
     
Parts Catalogue:
{'P101': 10, 'P102': 15, 'P103': 20, 'P104': 25, 'P105': 30}

Part Lookup:
P101: 10
P999: Unknown Part

Scrap Parts:
{'P105'}
IT6 – shoptools.py


def inspect(dia):
    """Classifies a diameter."""
    if dia < 10:
        return "Small"
    elif dia < 20:
        return "Medium"
    else:
        return "Large"


def tally(labels):
    """Counts the labels."""
    counts = {}

    for label in labels:
        counts[label] = counts.get(label, 0) + 1

    return counts


def report(shift, counts):
    """Creates a formatted shift report."""
    result = f"Shift {shift}: "

    for label, count in counts.items():
        result += f"{label} = {count}, "

    return result.rstrip(", ")
