from pydantic import BaseModel, Field
from typing import Optional

class DebtAnalysisResult(BaseModel):
    is_resolved: bool = Field(description="Describe si el cliente se comprometió a pagar la deuda o no")
    is_satisfied: bool = Field(description="Describe si el cliente se mostró satisfecho con el trato del asistente")
    promised_days: Optional[int] = Field(description="Número de días prometidos por el cliente para pagar la deuda. En caso de no especificar, se asumirá como indefinido.")
    effective_contact: Optional[bool] = Field(description="Indica si el contacto con el cliente fue efectivo. Tiene que ser la misma persona a la que se busca")