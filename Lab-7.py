class Machine:
    def __init__(self, name, capacity, rating, limit):
        self.name = name
        self.capacity = capacity
        self.rating = rating
        self.limit = limit
        self.jobs_completed = 0

    def process(self, job):
        if job <= self.limit:
            self.jobs_completed += 1
            print(f"{self.name} processed job: {job}")
        else:
            print(f"{self.name}: Job exceeds limit!")

    def __str__(self):
        return (f"Machine: {self.name}, "
                f"Capacity: {self.capacity}, "
                f"Rating: {self.rating}, "
                f"Limit: {self.limit}, "
                f"Jobs: {self.jobs_completed}")


# Create two machines
machine1 = Machine("Machine A", 100, 5, 50)
machine2 = Machine("Machine B", 200, 4, 80)

# Process jobs
machine1.process(30)
machine2.process(60)

# Print both machines
print(machine1)
print(machine2)

# Prove states are independent
machine1.process(40)

print("\nAfter updating Machine A:")
print(machine1)
print(machine2)
     
Machine A processed job: 30
Machine B processed job: 60
Machine: Machine A, Capacity: 100, Rating: 5, Limit: 50, Jobs: 1
Machine: Machine B, Capacity: 200, Rating: 4, Limit: 80, Jobs: 1
Machine A processed job: 40

After updating Machine A:
Machine: Machine A, Capacity: 100, Rating: 5, Limit: 50, Jobs: 2
Machine: Machine B, Capacity: 200, Rating: 4, Limit: 80, Jobs: 1
IT10 — Standard: The Guarded Machine


class Machine:
    def __init__(self, name, capacity, rating, limit):
        self.name = name
        self.capacity = capacity
        self.rating = rating
        self.limit = limit
        self.__jobs_completed = 0
        self.__total_processed = 0

    def operate(self, job):
        """Validates and processes a job within the machine limit."""
        if not isinstance(job, (int, float)):
            return "Invalid command: Job must be numeric."

        if job <= 0 or job > self.limit:
            return "Command rejected: Job is outside the allowed range."

        self.__jobs_completed += 1
        self.__total_processed += job

        return f"{self.name} successfully processed {job}."

    def status(self):
        """Returns machine status without changing its counters."""
        return {
            "Name": self.name,
            "Capacity": self.capacity,
            "Rating": self.rating,
            "Limit": self.limit,
            "Jobs Completed": self.__jobs_completed,
            "Total Processed": self.__total_processed
        }


# Create machine
machine = Machine("Machine A", 100, 5, 50)

# Valid and invalid operations
print(machine.operate(30))
print(machine.operate(60))
print(machine.operate(-5))

# Display status
print("\nMachine Status:")
print(machine.status())


# Demonstrate the colleague's bypass
# Python name-mangling is not a security boundary.
# An informed caller can still access the mangled attribute.
print("\nInternal attribute name:")
print(machine._Machine__jobs_completed)
     
Machine A successfully processed 30.
Command rejected: Job is outside the allowed range.
Command rejected: Job is outside the allowed range.

Machine Status:
{'Name': 'Machine A', 'Capacity': 100, 'Rating': 5, 'Limit': 50, 'Jobs Completed': 1, 'Total Processed': 30}

Internal attribute name:
1
IT8 — Fine: The Machine Runs a Batch



     

import random


class Machine:
    def __init__(self, name, capacity, rating, limit):
        self.name = name
        self.capacity = capacity
        self.rating = rating
        self.limit = limit
        self.__jobs_completed = 0
        self.__total_processed = 0

    def operate(self, job):
        """Processes a job if it is within the machine limit."""
        if not isinstance(job, (int, float)):
            return False

        if job <= 0 or job > self.limit:
            return False

        self.__jobs_completed += 1
        self.__total_processed += job

        return True

    def status(self):
        """Returns the machine's current statistics."""
        return {
            "Name": self.name,
            "Jobs Completed": self.__jobs_completed,
            "Total Processed": self.__total_processed
        }


# Create a machine
machine = Machine("Machine A", 100, 5, 50)

# Generate a batch of jobs
jobs = [random.randint(10, 60) for _ in range(10)]

print("Generated Jobs:", jobs)

# Process every job
for job in jobs:
    if machine.operate(job):
        print(f"Job {job}: Processed successfully")
    else:
        print(f"Job {job}: Rejected")

# Print shift report
print("\nSHIFT REPORT")
print("----------------------")

for key, value in machine.status().items():
    print(f"{key}: {value}")
     
Generated Jobs: [57, 53, 12, 21, 46, 39, 22, 15, 34, 48]
Job 57: Rejected
Job 53: Rejected
Job 12: Processed successfully
Job 21: Processed successfully
Job 46: Processed successfully
Job 39: Processed successfully
Job 22: Processed successfully
Job 15: Processed successfully
Job 34: Processed successfully
Job 48: Processed successfully

SHIFT REPORT
----------------------
Name: Machine A
Jobs Completed: 8
Total Processed: 237
IT6 — Precision: The Fleet


class Machine:
    def __init__(self, name, capacity, rating, limit):
        self.name = name
        self.capacity = capacity
        self.rating = rating
        self.limit = limit
        self.__jobs_completed = 0
        self.__total_processed = 0

    def operate(self, job):
        """Processes a valid job."""
        if not isinstance(job, (int, float)):
            return False

        if job <= 0 or job > self.limit:
            return False

        self.__jobs_completed += 1
        self.__total_processed += job

        return True

    def status(self):
        """Returns current machine statistics."""
        return {
            "Name": self.name,
            "Jobs Completed": self.__jobs_completed,
            "Total Processed": self.__total_processed
        }


def plant_report(machines):
    """Generates a complete plant report."""
    total_jobs = 0
    total_processed = 0

    print("\n========== PLANT REPORT ==========")

    for machine in machines:
        data = machine.status()

        print(f"\nMachine: {data['Name']}")
        print(f"Jobs Completed: {data['Jobs Completed']}")
        print(f"Total Processed: {data['Total Processed']}")

        total_jobs += data["Jobs Completed"]
        total_processed += data["Total Processed"]

    print("\n========== PLANT TOTAL ==========")
    print("Total Jobs:", total_jobs)
    print("Total Processed:", total_processed)
