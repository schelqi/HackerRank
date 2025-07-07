import operator

def person_lister(f):
    def inner(people):
        result = list()
        for person in people:
            person[2] = int(person[2])
        # Sort by age
        sorted_people = sorted(people, key=operator.itemgetter(2))
        for person in sorted_people:
            result.append(f(person))

        return result
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')