from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PlannerFormReference(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	formResponse: Optional[str] = Field(alias="formResponse", default=None,)
	formWebUrl: Optional[str] = Field(alias="formWebUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

