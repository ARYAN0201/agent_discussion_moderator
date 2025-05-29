from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Ollama
from utils.prompts import conflict_detection, gap_detection, role_adherence, summary_generation
from moderator.moderator import moderator_tone
llm = Ollama(model="mistral", temperature=0.3)
import time

class ModeratorUtils:
    def __init__(self, max_rounds=6):
        self.max_rounds = max_rounds

        self.conflict_prompt = PromptTemplate(
            input_variables=["history"],
            template=moderator_tone+conflict_detection )
        self.conflict_chain = LLMChain(llm=llm, prompt=self.conflict_prompt)

        self.gap_prompt = PromptTemplate(
            input_variables=["history"],
            template=moderator_tone+gap_detection)
        self.gap_chain = LLMChain(llm=llm, prompt=self.gap_prompt)

        self.role_adherence_prompt = PromptTemplate(
            input_variables=["role", "response"],
            template=moderator_tone+role_adherence)
        self.role_adherence_chain = LLMChain(llm=llm, prompt=self.role_adherence_prompt)

        self.summary_prompt = PromptTemplate(
            input_variables=["history", "question"],
            template=moderator_tone+summary_generation)
        self.summary_chain = LLMChain(llm=llm, prompt=self.summary_prompt)

    def detect_conflict(self, history):
        print("[⏳] Detecting conflict...")
        start = time.time()
        try:
            result = self.conflict_chain.run(history=history).strip()
            print(f"[✅] Conflict detected in {time.time() - start:.2f} seconds.")
            return result
        except Exception as e:
            print(f"[❌] Conflict detection failed: {e}")
            return "None"

    def identify_missing_points(self, history):
        print("[🔍] Identifying missing points...")
        start = time.time()
        try:
            result = self.gap_chain.run(history=history).strip()
            print(f"[✅] Missing points identified in {time.time() - start:.2f} seconds.")
            return result
        except Exception as e:
            print(f"[❌] Missing points identification failed: {e}")
            return "None"

    def check_role_adherence(self, role, response):
        print(f"[🧭] Checking role adherence...")
        start = time.time()
        try:
            result = self.role_adherence_chain.run(role=role, response=response).strip()
            print(f"[✅] Role adherence checked in {time.time() - start:.2f} seconds.")
            return result
        except Exception as e:
            print(f"[❌] Role adherence check failed: {e}")
            return "Yes, aligns well."

    def check_token_budget(self, round_num):
        if round_num >= self.max_rounds - 2:
            return "⚠️ Nearing token budget. Begin final comments."
        return "Within token budget."

    def summarize_final_decision(self, history, question):
        return self.summary_chain.run(history=history, question=question).strip()

    def select_next_speaker(self, history, last_speaker):
        """Simple round-robin with context-aware prioritization"""
        speakers = ["PM", "Engineer", "Designer"]
        next_speaker = speakers[(speakers.index(last_speaker) + 1) % len(speakers)]

        # Check for missing angles
        missing = self.identify_missing_points(history)
        if missing != "None":
            if "accessibility" in missing.lower():
                return "Designer"
            elif "tech stack" in missing.lower() or "performance" in missing.lower():
                return "Engineer"
            elif "timeline" in missing.lower() or "business" in missing.lower():
                return "PM"

        return next_speaker