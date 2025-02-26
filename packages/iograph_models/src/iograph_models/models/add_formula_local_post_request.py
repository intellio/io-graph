from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Add_formula_localPostRequest(BaseModel):
	name: Optional[str] = Field(default=None,alias="name",)
	formula: Optional[str] = Field(default=None,alias="formula",)
	comment: Optional[str] = Field(default=None,alias="comment",)


