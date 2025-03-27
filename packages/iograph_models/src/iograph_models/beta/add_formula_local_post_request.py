from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Add_formula_localPostRequest(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	formula: Optional[str] = Field(alias="formula", default=None,)
	comment: Optional[str] = Field(alias="comment", default=None,)


