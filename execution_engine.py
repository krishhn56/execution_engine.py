# Nexa Execution Layer - Execution Engine Prototype

def execute_plan(plan):

    print("\nExecuting Plan:\n")

    for step in plan:
        print("Running:", step)

    print("\nExecution Complete")


if __name__ == "__main__":

    sample_plan = [
        "Collect data",
        "Create document"
    ]

    execute_plan(sample_plan)
