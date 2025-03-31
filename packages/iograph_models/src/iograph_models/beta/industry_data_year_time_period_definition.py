from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IndustryDataYearTimePeriodDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.industryData.yearTimePeriodDefinition"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	endDate: Optional[str] = Field(alias="endDate", default=None,)
	startDate: Optional[str] = Field(alias="startDate", default=None,)
	year: Optional[IndustryDataYearReferenceValue] = Field(alias="year", default=None,)

from .industry_data_year_reference_value import IndustryDataYearReferenceValue
