from utils.summarizer import summarize_context

class ContextManager:
    def __init__(self):
        self.initial_query = ""
        self.history = []
        self.summary = ""
        self.round_count = 0

    def add_message(self, speaker, message):
        self.history.append(f"{speaker}: {message}")

    def update_round(self):
        self.round_count += 1
        if self.round_count % 3 == 0:
            self.summarize_and_reset()

    def summarize_and_reset(self):
        if not self.history:
            return
        summary = summarize_context(self.history)
        self.summary += f"\n[Round {self.round_count} Summary]: {summary}"
        self.history = [self.summary]

    def set_initial_query(self, query : str):
        self.initial_query = query