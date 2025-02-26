from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Im_subPostRequest(BaseModel):
	inumber1: Optional[str] = Field(default=None,alias="inumber1",)
	inumber2: Optional[str] = Field(default=None,alias="inumber2",)


