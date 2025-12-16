from agents.coordinator import Coordinator
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from memory.memory_agent import MemoryAgent

research = ResearchAgent()
analysis = AnalysisAgent()
memory = MemoryAgent()

manager = Coordinator(research, analysis, memory)

query = "Compare neural networks and transformers and recommend one"

print("User:", query)
response = manager.handle_query(query)
print("System:", response)