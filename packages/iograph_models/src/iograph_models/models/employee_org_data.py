from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EmployeeOrgData(BaseModel):
	costCenter: Optional[str] = Field(default=None,alias="costCenter",)
	division: Optional[str] = Field(default=None,alias="division",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


