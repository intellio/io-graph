from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Sum_sqPostRequest(BaseModel):
	values: Optional[str] = Field(default=None,alias="values",)


