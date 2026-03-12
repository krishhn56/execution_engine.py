# Nexa Execution Layer - Execution Engine Prototype

from context_manager import ContextManager

context = ContextManager()

def execute(task):
    context.update("last_task", task)
    print("Executing:", task)
