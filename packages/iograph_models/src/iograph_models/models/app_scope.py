from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AppScope(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	type: Optional[str] = Field(default=None,alias="type",)


