from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuditProperty(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	newValue: Optional[str] = Field(default=None,alias="newValue",)
	oldValue: Optional[str] = Field(default=None,alias="oldValue",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


