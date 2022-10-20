class API:
    @classmethod
    def get_rc(cls):
        with open('rc.txt', 'r') as file:
            lines = file.read().splitlines()
        return lines


def validate_rc():
    results = []
    rcs = API.get_rc()
    for rc in rcs:
        is_rc_valid = False
        if len(rc) == 10 and rc.isnumeric():  # ci string ma len cisla
            rc_int = int(rc)
            if rc_int % 11 == 0:
                is_rc_valid = True
        results.append((rc, is_rc_valid))
    return results


for i in validate_rc():
    if i[1]:
        print(f'{i[0]} is valid number')
    else:
        print(f'{i[0]} is not valid number')
