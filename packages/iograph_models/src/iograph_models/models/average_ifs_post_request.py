from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Average_ifsPostRequest(BaseModel):
	averageRange: Optional[str] = Field(default=None,alias="averageRange",)
	values: Optional[str] = Field(default=None,alias="values",)


