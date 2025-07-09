# University Course Scheduling with CSP

## Overview
This project implements a **Constraint Satisfaction Problem (CSP)** solver to create a university course schedule. The goal is to assign courses to specific classrooms, time slots, and instructors while ensuring no conflicts occur. The solution uses the **Backtracking** algorithm enhanced with **Forward Checking**, **Minimum Remaining Values (MRV)**, and **Least Constraining Value (LCV)** heuristics to optimize the scheduling process.

## Objective
The objective is to generate a valid course schedule that satisfies the following constraints:
- No two classes can be held in the same room at the same time.
- No instructor can teach two courses simultaneously.

## Features
- **CSP Modeling**: Models the scheduling problem as a CSP with courses as variables and combinations of rooms, time slots, and instructors as domains.
- **Backtracking Algorithm**: Uses backtracking to explore possible assignments systematically.
- **Forward Checking**: Reduces the domains of unassigned variables after each assignment to prevent future conflicts.
- **MRV Heuristic**: Selects the course with the fewest remaining valid assignments to reduce the search space.
- **LCV Heuristic**: Orders possible assignments to minimize constraints on other variables.
- **Sample Data**: Includes predefined courses (AI, Physics, Chemistry, Music, Cinema, Algebra), classrooms (Room1, Room2, Room3), time slots (9:00-10:00, 10:00-11:00, 11:00-12:00), and instructors.

## Installation
To run the project, you need Python 3.x installed. No additional libraries are required as the code uses standard Python modules (`itertools` and `collections`).

1. Clone or download the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```
3. Ensure you have the `main.py` file in the directory.

## Usage
1. Run the script using Python:
   ```bash
   python main.py
   ```
2. The program will output a valid schedule (if one exists) in the following format:
   ```
   Scheduling Solution:
   Physics: Room1 at 9:00-10:00 with Dr.Pouzesh
   Chemistry: Room1 at 10:00-11:00 with Dr.Fathi
   Algebra: Room1 at 11:00-12:00 with Dr.Pourbagheri
   AI: Room2 at 9:00-10:00 with Dr.Moosavi
   Music: Room2 at 10:00-11:00 with Dr.Shokoohi
   Cinema: Room2 at 11:00-12:00 with Dr.Mortazavi
   ```
3. If no valid schedule is found, the output will be:
   ```
   No solution found!
   ```

## Code Structure
- **main.py**: The main script containing the CSP solver implementation.
  - `instructors`: Dictionary mapping courses to their available instructors.
  - `classrooms`: List of available classrooms.
  - `time_slots`: List of available time slots.
  - `generate_domains()`: Creates all possible combinations of rooms, time slots, and instructors for each course.
  - `is_consistent()`: Checks if an assignment satisfies the constraints.
  - `select_unassigned_variable()`: Implements MRV to select the next course to assign.
  - `order_domain_values()`: Implements LCV to order possible assignments.
  - `forward_checking()`: Updates domains after an assignment to ensure consistency.
  - `backtrack()`: Core backtracking algorithm to find a valid solution.
  - `solve_schedule()`: Initializes and runs the solver.

## Constraints
- **Room-Time Conflict**: No two courses can be scheduled in the same room at the same time.
- **Instructor-Time Conflict**: No instructor can be assigned to two courses at the same time.

## Sample Output
The sample output provided in the project description demonstrates a valid schedule:
```
Physics: Room1 at 9:00-10:00 with Dr.Pouzesh
Chemistry: Room1 at 10:00-11:00 with Dr.Fathi
Algebra: Room1 at 11:00-12:00 with Dr.Pourbagheri
AI: Room2 at 9:00-10:00 with Dr.Moosavi
Music: Room2 at 10:00-11:00 with Dr.Shokoohi
Cinema: Room2 at 11:00-12:00 with Dr.Mortazavi
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License.

## Notes
- The project was designed as part of an academic assignment with a deadline of January 11, 2025, 23:59:59.
- The code is documented as required by the project specifications.