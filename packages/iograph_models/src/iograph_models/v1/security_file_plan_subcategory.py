from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityFilePlanSubcategory(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	odata_type: Literal["#microsoft.graph.security.filePlanSubcategory"] = Field(alias="@odata.type",)

