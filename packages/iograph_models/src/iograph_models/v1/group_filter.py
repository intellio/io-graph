from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class GroupFilter(BaseModel):
	includedGroups: Optional[list[str]] = Field(alias="includedGroups", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

