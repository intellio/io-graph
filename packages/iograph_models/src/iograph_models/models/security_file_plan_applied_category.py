from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityFilePlanAppliedCategory(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	subcategory: Optional[SecurityFilePlanSubcategory] = Field(default=None,alias="subcategory",)

from .security_file_plan_subcategory import SecurityFilePlanSubcategory

