from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ComplexPostRequest(BaseModel):
	realNum: Optional[str] = Field(default=None,alias="realNum",)
	iNum: Optional[str] = Field(default=None,alias="iNum",)
	suffix: Optional[str] = Field(default=None,alias="suffix",)


