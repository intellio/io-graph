from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Apply_custom_filterPostRequest(BaseModel):
	criteria1: Optional[str] = Field(default=None,alias="criteria1",)
	criteria2: Optional[str] = Field(default=None,alias="criteria2",)
	oper: Optional[str] = Field(default=None,alias="oper",)


