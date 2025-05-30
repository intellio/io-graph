from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ClearPostRequest(BaseModel):
	applyTo: Optional[str] = Field(alias="applyTo", default=None,)

