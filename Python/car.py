class Car:
    def __init__(self, model, year, cc, is_running):
        self.model = model
        self.year = year
        self.cc = cc
        self.is_running = is_running

    def drive(self):
        print(f"You drive the {self.model}")

    def stop(self):
        print(f"You stop the {self.model}")

    def describe(self):
        print(f"{self.model} {self.year} {self.cc} {self.is_running}")

