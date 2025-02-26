from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Skew_pPostRequest(BaseModel):
	values: Optional[str] = Field(default=None,alias="values",)


