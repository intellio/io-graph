from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DatevaluePostRequest(BaseModel):
	dateText: Optional[str] = Field(alias="dateText", default=None,)

