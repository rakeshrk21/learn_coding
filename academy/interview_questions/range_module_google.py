class RangeModule:

    def __init__(self):
        self.myList = list()

    def add_range(self, left: int, right: int) -> None:
        if right > left:
            for i in range(left, right + 1):
                if i not in self.myList:
                    self.myList.append(i)
        self.myList.sort()
        print(self.myList)

    def query_range(self, left: int, right: int) -> bool:
        found = True
        for i in range(left, right):
            if i not in self.myList:
                found = False
                break
        return found

    def remove_range(self, left: int, right: int) -> None:
        for i in range(left, right):
            if i in self.myList:
                self.myList.remove(i)
        print(self.myList)


obj = RangeModule()
obj.add_range(10, 20)
obj.remove_range(14, 16)
print(obj.query_range(10, 14))
obj.add_range(14, 16)
print(list(range(25, 25)))
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)