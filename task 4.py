# Rule-Based Expert System
# Student Academic Guidance using Backward Chaining

# Facts about the student
facts = {
    "GoodAttendance",
    "CompletedAssignments",
    "PassedInternalExam",
    "RegularPractice"
}

# Rules
rules = {
    "GoodAcademicPerformance": [
        ["PassedInternalExam", "CompletedAssignments"]
    ],

    "EligibleForPlacement": [
        ["GoodAcademicPerformance", "GoodAttendance"]
    ],

    "NeedsExtraPractice": [
        ["PassedInternalExam", "not RegularPractice"]
    ],

    "ReadyForInterview": [
        ["EligibleForPlacement", "RegularPractice"]
    ]
}


# Backward Chaining function
def backward_chaining(goal, visited=None):

    if visited is None:
        visited = set()

    print("Trying to prove:", goal)

    # If goal is already a fact
    if goal in facts:
        print("  Fact found:", goal)
        return True

    # Avoid repeated checking
    if goal in visited:
        return False

    visited.add(goal)

    # If there is no rule for the goal
    if goal not in rules:
        print("  No rule found for:", goal)
        return False

    # Check each rule
    for conditions in rules[goal]:

        print("  Rule for", goal, "requires:", conditions)

        all_true = True

        for condition in conditions:

            # Handle negative condition
            if condition.startswith("not "):
                fact_name = condition[4:]

                if fact_name in facts:
                    all_true = False
                    print("  Condition failed:", condition)
                else:
                    print("  Condition satisfied:", condition)

            else:
                if not backward_chaining(condition, visited):
                    all_true = False
                    break

        if all_true:
            print("  Goal proved:", goal)
            return True

    print("  Goal cannot be proved:", goal)
    return False


# Selected goal
goal = "EligibleForPlacement"

print("STUDENT ACADEMIC GUIDANCE")
print("--------------------------")
print("Facts:")
for fact in facts:
    print("-", fact)

print("\nSelected Goal:", goal)
print("\nReasoning Steps:")
result = backward_chaining(goal)

print("\nFinal Conclusion:")
if result:
    print(goal, "-> PROVED")
else:
    print(goal, "-> NOT PROVED")