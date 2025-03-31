from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PositionDetail(BaseModel):
	company: Optional[CompanyDetail] = Field(alias="company", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	endMonthYear: Optional[str] = Field(alias="endMonthYear", default=None,)
	jobTitle: Optional[str] = Field(alias="jobTitle", default=None,)
	layer: Optional[int] = Field(alias="layer", default=None,)
	level: Optional[str] = Field(alias="level", default=None,)
	role: Optional[str] = Field(alias="role", default=None,)
	secondaryJobTitle: Optional[str] = Field(alias="secondaryJobTitle", default=None,)
	secondaryRole: Optional[str] = Field(alias="secondaryRole", default=None,)
	startMonthYear: Optional[str] = Field(alias="startMonthYear", default=None,)
	summary: Optional[str] = Field(alias="summary", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .company_detail import CompanyDetail
