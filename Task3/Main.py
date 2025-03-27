import random

def min(x):
    return (x-3)**2

def max(x):
    return -x**2+3

def random_number():
    return random.randint(-10, 10)

def mutate(current):
    return current+random.choice([-1,1])

def RHS_min():
    min_value = random_number()
    current_function = min(min_value)
    while True:
        print(f"Current min value: x = {min_value}, function f(x): {current_function}")
        if current_function == 0:
            print(f"Minimum value {current_function}\n")
            break
        new_min = mutate(min_value)
        new_current_min = min(new_min)
        if new_current_min < current_function:
            min_value = new_min
            current_function = new_current_min

def RHS_max():
    max_value = random_number()
    current_function = max(max_value)
    while True:
        print(f"Current max value : x = {max_value}, function f(x): {current_function}")
        if current_function == 3:
            print(f"Maximium value {current_function}")
            break
        new_max = mutate(max_value)
        new_current_max = max(new_max)
        if new_current_max > current_function:
            max_value = new_max
            current_function = new_current_max

def objective_function_maximize(selected_projects, projects):
    total_benefit = 0
    total_resources = 0

    for project in selected_projects:
        total_resources += projects[project]["resources"]
        total_benefit += projects[project]["benefit"]

    if total_resources > 100:
        return float('-inf')
    return total_benefit

def objective_function_minimize(selected_projects, projects):
    total_time = 0
    total_resources = 0

    for project in selected_projects:
        total_resources += projects[project]["resources"]
        total_time += projects[project]["time"]

    if total_resources > 100:
        return float('inf')
    return total_time

def generate_random_solution(project_ids):
    num_projects = len(project_ids)
    return random.sample(project_ids, random.randint(1,num_projects))


def mutate_solution(current_solution, project_ids):
    new_solution = current_solution.copy()

    mutation_type = random.choice(['add', 'remove', 'swap'])

    if mutation_type == 'add':
        num_projects_to_add = random.randint(1, len(project_ids)//2)
        for _ in range(num_projects_to_add):
            new_project = random.choice(project_ids)
            if new_project not in new_solution:
                new_solution.append(new_project)
    elif mutation_type == 'remove':
        num_projects_to_remove = random.randint(1, max(1, len(new_solution)//2))
        for _ in range(num_projects_to_remove):
            if new_solution:
                project_to_remove = random.choice(new_solution)
                new_solution.remove(project_to_remove)
    elif mutation_type == 'swap':
        if new_solution:
            project_to_remove = random.choice(new_solution)
            new_solution.remove(project_to_remove)
            project_to_add = random.choice(project_ids)
            while project_to_add in new_solution:
                project_to_add = random.choice(project_ids)
            new_solution.append(project_to_add)

    if not new_solution:
        new_solution.append(random.choice(project_ids))

    return new_solution

def RHC(projects, objective_function, minimize=False):
    project_ids = list(projects.keys())

    best_solution = generate_random_solution(project_ids)
    best_score = objective_function(best_solution, projects)

    no_improvement_iterations = 0
    max_iterations_without_improvement = 25

    while no_improvement_iterations < max_iterations_without_improvement:
        print(f"Current best solution: {best_solution}, Score: {best_score}")

        new_solution = mutate_solution(best_solution, project_ids)
        new_score = objective_function(new_solution, projects)

        if new_score == float('-inf') or new_score == float('inf'):
            no_improvement_iterations += 1
            continue

        if minimize:
            if new_score < best_score:
                best_solution = new_solution
                best_score = new_score
                no_improvement_iterations = 0
            else:
                no_improvement_iterations += 1
        else:
            if new_score > best_score:
                best_solution = new_solution
                best_score = new_score
                no_improvement_iterations = 0
            else:
                no_improvement_iterations += 1

if __name__ == '__main__':
    RHS_min()
    RHS_max()

    #Set 2
    #maximize total benefit
    testcase1: {
        'A': {"units": 20, "benefit": 40},
        'B': {"units": 30, "benefit": 50},
        'C': {"units": 25, "benefit": 30},
        'D': {"units": 15, "benefit": 25}
    }
    testcase2: {# minimize total Est.time
        'A': {"units": 10, "time": 15} ,
        'B': {"units": 40, "time": 60},
        'C': {"units": 20, "time": 30},
        'D': {"units": 25, "time": 35},
        'E': {"units": 5, "time": 10},
    }
    testcase3: {  # maximize total benefit
        'X': {"units": 50, "benefit": 80},
        'Y': {"units": 30, "benefit": 45},
        'Z': {"units": 15, "benefit": 20},
        'W': {"units": 25, "benefit": 35}
    }
print("\n")

print("Randomized Hill Climbing for Resource Allocation Test Case 1 :")
RHC(testcase1, objective_function_maximize)
print("\n")
print("Randomized Hill Climbing for Resource Allocation Test Case 2 :")
RHC(testcase2, objective_function_maximize, minimize=True)
print("\n")
print("Randomized Hill Climbing for Resource Allocation Test Case 3 :")
RHC(testcase3, objective_function_maximize)
print("\n")

