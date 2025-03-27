from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Atan2PostRequest(BaseModel):
	xNum: Optional[str] = Field(alias="xNum", default=None,)
	yNum: Optional[str] = Field(alias="yNum", default=None,)


