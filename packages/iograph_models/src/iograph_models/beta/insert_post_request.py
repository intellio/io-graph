from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InsertPostRequest(BaseModel):
	shift: Optional[str] = Field(alias="shift", default=None,)

