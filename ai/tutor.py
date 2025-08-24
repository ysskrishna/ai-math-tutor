from models.models import MathReasoning
from ai.client import get_openai_client

def get_step_by_step_solution(problem: str):
    model = get_openai_client().with_structured_output(MathReasoning)

    return model.invoke(problem)