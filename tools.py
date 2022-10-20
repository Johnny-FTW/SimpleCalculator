class API:
    @classmethod
    def get_data(cls):  # staticka,nema pristup k ostanym metodam, iba k atributom
        file = open("nums.txt", "r")
        return file.read().splitlines()  # odtrhne \n ["1,1", "1.5...."


def load_nums_from_file():
    nums = []
    lines = API.get_data()
    for line in lines:
        pair = line.split(",")  # ["1", "1"]
        if len(pair) == 2:
            x = float(pair[0].strip())  # strip zrusi medzery
            y = float(pair[1].strip())
            nums.append((x, y))  # [(x,y),(x,y)...] tule v liste
    return nums
