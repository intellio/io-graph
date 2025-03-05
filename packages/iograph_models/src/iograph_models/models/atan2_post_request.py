from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Atan2PostRequest(BaseModel):
	xNum: Optional[str] = Field(default=None,alias="xNum",)
	yNum: Optional[str] = Field(default=None,alias="yNum",)


