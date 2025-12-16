import datetime

class MemoryAgent:
    def __init__(self):
        self.conversation = []
        self.knowledge_base = []

    def store(self, topic, content, source):
        record = {
            "time": str(datetime.datetime.now()),
            "topic": topic,
            "content": content,
            "source": source
        }
        self.knowledge_base.append(record)

    def search(self, keyword):
        results = []
        for item in self.knowledge_base:
            if keyword.lower() in item["topic"].lower():
                results.append(item)
        return results