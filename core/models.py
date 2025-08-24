
from pydantic import BaseModel, Field

class Step(BaseModel):
    step_number: int = Field(description="The step number in the solution")
    explanation: str = Field(description="The explanation for the step")
    output: str = Field(description="The output of the step")

class MathReasoning(BaseModel):
    steps: list[Step] = Field(description="Step-by-step solution")
    final_answer: str = Field(description="The final answer to the problem")