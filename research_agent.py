class ResearchAgent:
    def __init__(self):
        self.data = {
            "neural networks": "CNN, RNN, and Transformers are main types.",
            "transformers": "Transformers use self-attention and are efficient for NLP.",
            "reinforcement learning": "RL learns by reward and punishment."
        }

    def research(self, query):
        query = query.lower()
        for key in self.data:
            if key in query:
                return self.data[key]
        return "No data found."