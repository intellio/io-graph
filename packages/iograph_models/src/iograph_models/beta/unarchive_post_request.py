from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnarchivePostRequest(BaseModel):
	justification: Optional[str] = Field(alias="justification", default=None,)

