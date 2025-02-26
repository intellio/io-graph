from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnarchivePostResponse(BaseModel):
	value: Optional[bool] = Field(default=None,alias="value",)


