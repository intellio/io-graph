from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeletePostRequest(BaseModel):
	shift: Optional[str] = Field(alias="shift", default=None,)

