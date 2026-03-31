# Nexa Execution Layer - Execution Engine Prototype

from context_manager import ContextManager

context = ContextManager()

def execute(task):
    context.update("last_task", task)
    print("Executing:", task)
def execute(task, context=None):
    if context:
        task = enhance_task_with_context(task, context)

    return run_task(task)


def enhance_task_with_context(task, context):
    # simple example
    task["context"] = context
    return task
