import abc


class Observer:
    @abc.abstractmethod
    def update(self, value):
        pass


class SimpleObserver(Observer):
    def __init__(self, name, subject):
        self.value = 0
        self.name = name
        self.subject = subject
        subject.registerObserver(self)

    def update(self, value):
        self.value = value
        self.display()

    def display(self):
        print(f"{self.name} value: {self.value}")

    def run_process(self):
        print(f"{self.name} run process value: {self.value}")
