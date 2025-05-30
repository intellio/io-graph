from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SpecialFolder(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

