from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IndustryDataAdditionalClassGroupOptions(BaseModel):
	createTeam: Optional[bool] = Field(alias="createTeam", default=None,)
	writeDisplayNameOnCreateOnly: Optional[bool] = Field(alias="writeDisplayNameOnCreateOnly", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

