from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Is_formulaPostRequest(BaseModel):
	reference: Optional[str] = Field(alias="reference", default=None,)

