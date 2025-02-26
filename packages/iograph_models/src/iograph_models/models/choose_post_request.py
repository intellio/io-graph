from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChoosePostRequest(BaseModel):
	indexNum: Optional[str] = Field(default=None,alias="indexNum",)
	values: Optional[str] = Field(default=None,alias="values",)


