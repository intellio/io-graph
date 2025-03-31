from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RowsPostRequest(BaseModel):
	array: Optional[str] = Field(alias="array", default=None,)

