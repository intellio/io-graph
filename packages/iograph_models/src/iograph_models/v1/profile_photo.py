from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ProfilePhoto(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.profilePhoto"] = Field(alias="@odata.type", default="#microsoft.graph.profilePhoto")
	height: Optional[int] = Field(alias="height", default=None,)
	width: Optional[int] = Field(alias="width", default=None,)

