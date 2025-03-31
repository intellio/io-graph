from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ProfileSource(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.profileSource"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)

