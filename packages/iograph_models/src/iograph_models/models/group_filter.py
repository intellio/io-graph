from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GroupFilter(BaseModel):
	includedGroups: Optional[list[str]] = Field(default=None,alias="includedGroups",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


