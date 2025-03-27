from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerFormsRequirement(BaseModel):
	requiredForms: Optional[list[str]] = Field(alias="requiredForms", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


