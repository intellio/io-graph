from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SubtotalPostRequest(BaseModel):
	functionNum: Optional[str] = Field(default=None,alias="functionNum",)
	values: Optional[str] = Field(default=None,alias="values",)


