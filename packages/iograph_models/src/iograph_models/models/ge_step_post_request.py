from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Ge_stepPostRequest(BaseModel):
	number: Optional[str] = Field(alias="number",default=None,)
	step: Optional[str] = Field(alias="step",default=None,)


