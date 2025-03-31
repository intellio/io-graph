from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Package(BaseModel):
	type: Optional[str] = Field(alias="type", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

