from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class XnpvPostRequest(BaseModel):
	rate: Optional[str] = Field(default=None,alias="rate",)
	values: Optional[str] = Field(default=None,alias="values",)
	dates: Optional[str] = Field(default=None,alias="dates",)


