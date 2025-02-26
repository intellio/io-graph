from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ImaginaryPostRequest(BaseModel):
	inumber: Optional[str] = Field(default=None,alias="inumber",)


