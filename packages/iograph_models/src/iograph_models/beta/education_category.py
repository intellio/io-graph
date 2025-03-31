from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class EducationCategory(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.educationCategory"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)

