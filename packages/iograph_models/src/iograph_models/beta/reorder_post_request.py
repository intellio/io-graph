from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ReorderPostRequest(BaseModel):
	priority: Optional[int] = Field(alias="priority", default=None,)

