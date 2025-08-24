from models.models import MathReasoning
from ai.client import get_openai_client
from ai.prompts import SYSTEM_PROMPT, USER_PROMPT
from langchain_core.messages import SystemMessage, HumanMessage

def get_step_by_step_solution(problem: str):
    model = get_openai_client().with_structured_output(MathReasoning)
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=USER_PROMPT.format(problem=problem))
    ]
    return model.invoke(messages)