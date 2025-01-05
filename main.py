from itertools import product
from collections import defaultdict

instructors = {
"AI": ["Dr.Moosavi","Dr.Shahabi"],
"Physics": ["Dr.Pouzesh"],
"Chemistry": ["Dr.Fathi"],
"Music": ["Dr.Shokoohi","Dr.Mortazavi"],
"Cinema": ["Dr.Mortazavi","Dr.Khosravani"],
"Algebra": ["Dr.Pourbagheri"]
}
classrooms = ["Room1", "Room2", "Room3"]
time_slots = ["9:00-10:00", "10:00-11:00", "11:00-12:00"]



def generate_domains():
    domains = {}
    for course, teachers in instructors.items():
        domains[course] = list(product(classrooms, time_slots, teachers))
    return domains

def is_consistent(assignment, course, value):
    """محدودیت‌ها"""
    room, time, teacher = value
    for assigned_course, (assigned_room, assigned_time, assigned_teacher) in assignment.items():
        if room == assigned_room and time == assigned_time:
            return False
        if teacher == assigned_teacher and time == assigned_time:
            return False
    return True

def select_unassigned_variable(domains, assignment):
    """MRV"""
    unassigned = [var for var in domains if var not in assignment]
    return min(unassigned, key=lambda var: len(domains[var]))

def order_domain_values(variable, domains, assignment):
    """LCV"""
    def count_conflicts(value):
        room, time, teacher = value
        conflicts = 0
        for var in domains:
            if var in assignment:
                continue
            for val in domains[var]:
                if val[0] == room and val[1] == time:
                    conflicts += 1
                if val[2] == teacher and val[1] == time:
                    conflicts += 1
        return conflicts

    return sorted(domains[variable], key=count_conflicts)


def forward_checking(domains, variable, value):
    """Forward Checking"""
    room, time, teacher = value
    new_domains = defaultdict(list, {var: list(vals) for var, vals in domains.items()})

    for var in domains:
        if var == variable:
            continue
        new_domains[var] = [
            val for val in domains[var]
            if (val[0] != room or val[1] != time) and
               (val[2] != teacher or val[1] != time)
        ]

        if not new_domains[var]:
            return None

    return new_domains

def backtrack(assignment, domains):
    """Backtracking"""
    if len(assignment) == len(instructors):
        return assignment

    variable = select_unassigned_variable(domains, assignment)
    for value in order_domain_values(variable, domains, assignment):
        if is_consistent(assignment, variable, value):
            assignment[variable] = value
            new_domains = forward_checking(domains, variable, value)

            if new_domains is not None:
                result = backtrack(assignment, new_domains)
                if result:
                    return result

            del assignment[variable]

    return None

def solve_schedule():
    domains = generate_domains()
    assignment = {}
    result = backtrack(assignment, domains)
    return result

solution = solve_schedule()

if solution:
    print("Scheduling Solution:")
    for course, (room, time, teacher) in solution.items():
        print(f"{course}: {room} at {time} with {teacher}")
else:
    print("No solution found!")
