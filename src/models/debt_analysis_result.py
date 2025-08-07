from pydantic import BaseModel, Field

class DebtAnalysisResult(BaseModel):
    is_resolved: bool = Field(description="Describe si el cliente se comprometió a pagar la deuda o no")