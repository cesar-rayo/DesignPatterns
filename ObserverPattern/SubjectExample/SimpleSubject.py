from ObserverPattern.SubjectExample.Subject import Subject


class SimpleSubject(Subject):
    def __init__(self):
        self.observers = []
        self.value = 0

    def registerObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.value)

    def changeValue(self, value):
        print(f"Changed subject value from {self.value} to {value}")
        self.value = value
        self.notifyObservers()
