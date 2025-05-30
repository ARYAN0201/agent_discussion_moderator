from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Ollama

llm = Ollama(model="mistral", temperature=0.3)

moderator_tone = """
You are a calm, strategic, and unbiased moderator overseeing a technical product discussion between a PM, Engineer, and Designer.
You always speak concisely, highlight key tensions or gaps, and help keep the conversation on track toward decision-making.
You never take sides, but you ensure alignment with business, technical, and user goals.
"""

moderator_prompt = PromptTemplate(
    input_variables=["history", "comment"],
    template="""
{tone}

Context so far:
{history}

Moderator’s Comment:
{comment}
"""
)

moderator_chain = LLMChain(llm=llm, prompt=moderator_prompt)

def respond_as_moderator(history, comment):
    return moderator_chain.run(history=history, comment=comment, tone=moderator_tone).strip()