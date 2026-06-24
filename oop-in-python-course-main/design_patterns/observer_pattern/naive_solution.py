# Spreadsheet 2: calculates the total
class Sheet2:
    def __init__(self) -> None:
        self.total = 0

    def calculate_total(self, values: list[float]) -> float:
        sum = 0
        for value in values:
            sum += value

        self.total = sum
        print(f"New total: {sum}")
        return self.total


# Spreadsheet 1: contains the data source and bar chart
class BarChart:
    def render(self, values: list[float]) -> None:
        print("Rendering bar chart with new values")


class DataSource:
    def __init__(self) -> None:
        self._values: list[float] = []
        self.dependents: list[object] = []

    @property
    def values(self) -> list[float]:
        return self._values

    @values.setter
    def values(self, values: list[float]) -> None:
        self._values = values

        # Update dependencies -- this is gonna get very messy as we add more dependencies!
        for dependent in self.dependents:
            if isinstance(dependent, Sheet2):
                dependent.calculate_total(values)
            elif isinstance(dependent, BarChart):
                dependent.render(values)

    def addDependent(self, dependent: object) -> None:
        self.dependents.append(dependent)

    def removeDependent(self, dependent: object) -> None:
        self.dependents.remove(dependent)


# Example useage
sheet = Sheet2()
barChart = BarChart()

dataSource = DataSource()
dataSource.addDependent(sheet)
dataSource.addDependent(barChart)

# Setting the values triggers the total and bar chart to also be updated:
dataSource.values = [1, 2, 3, 4.1]
# Logs:
# New total: 10.1
# Rendering bar chart with new values

print("Removing Bar chart...")
dataSource.removeDependent(barChart)
dataSource.values = [10, 1]
# Logs:
# New total: 11
