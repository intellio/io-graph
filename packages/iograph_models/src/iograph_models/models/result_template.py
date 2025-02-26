from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ResultTemplate(BaseModel):
	body: Optional[str] = Field(default=None,alias="body",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


