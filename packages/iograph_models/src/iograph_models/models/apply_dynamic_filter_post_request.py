from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Apply_dynamic_filterPostRequest(BaseModel):
	criteria: Optional[str] = Field(default=None,alias="criteria",)


