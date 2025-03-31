from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ColumnsPostRequest(BaseModel):
	array: Optional[str] = Field(alias="array", default=None,)

