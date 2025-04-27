# Simple Map Coloring using Backtracking

# Graph of regions and neighbors
Graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'V', 'SA'],
    'V': ['NSW', 'SA'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'T': []
}

# User-defined number of colors
n = int(input("Enter number of colors: "))
#colors = [input(f"Color {i+1}: ") for i in range(n)]

for i in range(n):
    colors = input("color  : ")

backtrack_count = 0  # Count how many times we backtrack

# Check if color assignment is valid
def is_safe(assignment, region, color):
    for neighbor in Graph[region]:
        if assignment.get(neighbor) == color:
            return False
    return True

# Backtracking function
def solve(assignment):
    global backtrack_count

    if len(assignment) == len(Graph):
        return assignment

    for region in Graph:
        if region not in assignment:
            for color in colors:
                print(f"Trying {color} for {region}")
                if is_safe(assignment, region, color):
                    assignment[region] = color
                    result = solve(assignment)
                    if result:
                        return result
                    assignment.pop(region)
                    backtrack_count += 1
                    print(f"Backtracking on {region}")
            break

    return None

# Solve the problem
solution = solve({})
print("\nFinal Solution:", solution)
print("Total Backtracks:", backtrack_count)
