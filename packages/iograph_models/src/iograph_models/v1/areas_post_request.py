from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AreasPostRequest(BaseModel):
	reference: Optional[str] = Field(alias="reference", default=None,)

