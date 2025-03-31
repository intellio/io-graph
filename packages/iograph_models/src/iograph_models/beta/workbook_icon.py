from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookIcon(BaseModel):
	index: Optional[int] = Field(alias="index", default=None,)
	set: Optional[str] = Field(alias="set", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

