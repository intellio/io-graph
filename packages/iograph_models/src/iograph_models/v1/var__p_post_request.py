from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Var__pPostRequest(BaseModel):
	values: Optional[str] = Field(alias="values", default=None,)

