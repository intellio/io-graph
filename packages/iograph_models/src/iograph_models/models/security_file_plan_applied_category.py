from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityFilePlanAppliedCategory(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	subcategory: Optional[SecurityFilePlanSubcategory] = Field(alias="subcategory",default=None,)

from .security_file_plan_subcategory import SecurityFilePlanSubcategory

