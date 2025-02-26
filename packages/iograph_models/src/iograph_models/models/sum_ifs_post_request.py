from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Sum_ifsPostRequest(BaseModel):
	sumRange: Optional[str] = Field(default=None,alias="sumRange",)
	values: Optional[str] = Field(default=None,alias="values",)


