from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IndustryDataAggregatedInboundStatistics(BaseModel):
	errors: Optional[int] = Field(alias="errors", default=None,)
	groups: Optional[int] = Field(alias="groups", default=None,)
	matchedPeopleByRole: Optional[list[IndustryDataIndustryDataRunRoleCountMetric]] = Field(alias="matchedPeopleByRole", default=None,)
	memberships: Optional[int] = Field(alias="memberships", default=None,)
	organizations: Optional[int] = Field(alias="organizations", default=None,)
	people: Optional[int] = Field(alias="people", default=None,)
	unmatchedPeopleByRole: Optional[list[IndustryDataIndustryDataRunRoleCountMetric]] = Field(alias="unmatchedPeopleByRole", default=None,)
	warnings: Optional[int] = Field(alias="warnings", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .industry_data_industry_data_run_role_count_metric import IndustryDataIndustryDataRunRoleCountMetric
