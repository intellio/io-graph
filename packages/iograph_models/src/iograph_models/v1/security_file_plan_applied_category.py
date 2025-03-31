from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityFilePlanAppliedCategory(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	odata_type: Literal["#microsoft.graph.security.filePlanAppliedCategory"] = Field(alias="@odata.type",)
	subcategory: Optional[SecurityFilePlanSubcategory] = Field(alias="subcategory", default=None,)

from .security_file_plan_subcategory import SecurityFilePlanSubcategory
