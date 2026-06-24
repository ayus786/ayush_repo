from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update() -> None:
        pass

class Sheet2(Observer):
    def __init__(self, dataSource) -> None:
        self.total = 0
        self.dataSource = dataSource

    def update(self):
        self.total = self.calculate_total(self.dataSource.values)
        print(f"New total: {self.total}")

    def calculate_total(self, values: list[float]) -> float:
        sum = 0
        for value in values:
            sum += value

        self.total = sum
        return self.total

class BarChart(Observer):
    def __init__(self, dataSource) -> None:
        self.dataSource = dataSource

    def update(self):
        print("Rendering bar chart with new values")

# Our observer manager class
class Subject:
    def __init__(self) -> None:
        self.observers: list[Observer] = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for obs in self.observers:
            obs.update()  # polymorphism -- we can treat all observers the same

class DataSource(Subject):
    def __init__(self) -> None:
        super().__init__()  # Initialize observers from ObserverManager
        self._values: list[float] = []

    @property
    def values(self) -> list[float]:
        return self._values

    @values.setter
    def values(self, values: list[float]) -> None:
        self._values = values
        super().notify_observers()

dataSource = DataSource()
sheetTotal = Sheet2(dataSource)
barChart = BarChart(dataSource)

dataSource.add_observer(sheetTotal)
dataSource.add_observer(barChart)

print(dataSource.values)  # []

dataSource.values = [1, 2, 3, 4.1]
# LOGS:
# New total: 10.1
# Rendering bar chart with new values
