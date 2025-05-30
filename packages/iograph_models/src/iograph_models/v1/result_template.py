from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ResultTemplate(BaseModel):
	body: Optional[str] = Field(alias="body", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

