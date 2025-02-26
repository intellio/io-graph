from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Im_log2PostRequest(BaseModel):
	inumber: Optional[str] = Field(default=None,alias="inumber",)


