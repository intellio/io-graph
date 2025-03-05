from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Im_divPostRequest(BaseModel):
	inumber1: Optional[str] = Field(default=None,alias="inumber1",)
	inumber2: Optional[str] = Field(default=None,alias="inumber2",)


