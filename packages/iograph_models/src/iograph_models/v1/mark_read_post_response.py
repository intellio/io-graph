from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Mark_readPostResponse(BaseModel):
	value: Optional[bool] = Field(alias="value", default=None,)

