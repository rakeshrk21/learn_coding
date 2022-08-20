class Towers:
    def __init__(self, disks=3):
        self.disks = disks
        self.towers = [[]] * 3
        self.towers[0] = [i for i in range(self.disks, 0, -1)]
        self.towers[1] = []
        self.towers[2] = []

    def __str__(self):
        output = ""
        for i in range(self.disks, -1, -1):
            for j in range(3):
                if len(self.towers[j]) > i:
                    output += " " + str(self.towers[j][i])
                else:
                    output += "  "
        output += "\n"

        return output + "-------"


t = Towers(3)
print(t)
