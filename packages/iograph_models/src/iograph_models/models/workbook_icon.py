from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookIcon(BaseModel):
	index: Optional[int] = Field(default=None,alias="index",)
	set: Optional[str] = Field(default=None,alias="set",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


