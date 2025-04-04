from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Average_ifsPostRequest(BaseModel):
	averageRange: Optional[str] = Field(alias="averageRange", default=None,)
	values: Optional[str] = Field(alias="values", default=None,)

