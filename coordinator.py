class Coordinator:
    def __init__(self, research, analysis, memory):
        self.research = research
        self.analysis = analysis
        self.memory = memory

    def handle_query(self, query):
        print("[Coordinator] Received query")

        if "earlier" in query.lower() or "discuss" in query.lower():
            return self.memory.search("neural")

        research_result = self.research.research(query)
        print("[ResearchAgent] Done")

        if "analyze" in query.lower() or "compare" in query.lower():
            analysis_result = self.analysis.analyze(research_result)
            self.memory.store(query, analysis_result, "AnalysisAgent")
            return analysis_result

        self.memory.store(query, research_result, "ResearchAgent")
        return research_result