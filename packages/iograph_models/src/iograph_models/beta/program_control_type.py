from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ProgramControlType(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.programControlType"] = Field(alias="@odata.type",)
	controlTypeGroupId: Optional[str] = Field(alias="controlTypeGroupId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)

