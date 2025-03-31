from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EmployeeOrgData(BaseModel):
	costCenter: Optional[str] = Field(alias="costCenter", default=None,)
	division: Optional[str] = Field(alias="division", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

