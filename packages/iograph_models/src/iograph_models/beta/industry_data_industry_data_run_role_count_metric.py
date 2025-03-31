from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IndustryDataIndustryDataRunRoleCountMetric(BaseModel):
	count: Optional[int] = Field(alias="count", default=None,)
	role: Optional[str] = Field(alias="role", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

