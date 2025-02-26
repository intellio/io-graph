from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Im_secPostRequest(BaseModel):
	inumber: Optional[str] = Field(default=None,alias="inumber",)


