from web_context_analyzer import analyze_webpage

class ExecutionEngine:

    def process_web_context(self, context_manager):
        web_data = context_manager.get_web_context()

        if not web_data:
            return {"error": "No web context found"}

        content = web_data["content"]

        # 🔥 AI Analysis
        result = analyze_webpage(content)

        return result
