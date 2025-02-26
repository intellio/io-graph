from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MoveAction(BaseModel):
	from_: Optional[str] = Field(default=None,alias="from",)
	to: Optional[str] = Field(default=None,alias="to",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


