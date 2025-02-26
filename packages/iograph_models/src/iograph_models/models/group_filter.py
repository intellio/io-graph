from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class GroupFilter(BaseModel):
	includedGroups: list[Optional[str]] = Field(alias="includedGroups",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


