from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataInboundActivityResults(BaseModel):
	activityId: Optional[str] = Field(alias="activityId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	status: Optional[IndustryDataIndustryDataActivityStatus | str] = Field(alias="status", default=None,)
	odata_type: Literal["#microsoft.graph.industryData.inboundActivityResults"] = Field(alias="@odata.type", default="#microsoft.graph.industryData.inboundActivityResults")
	errors: Optional[int] = Field(alias="errors", default=None,)
	groups: Optional[IndustryDataIndustryDataRunEntityCountMetric] = Field(alias="groups", default=None,)
	matchedPeopleByRole: Optional[list[IndustryDataIndustryDataRunRoleCountMetric]] = Field(alias="matchedPeopleByRole", default=None,)
	memberships: Optional[IndustryDataIndustryDataRunEntityCountMetric] = Field(alias="memberships", default=None,)
	organizations: Optional[IndustryDataIndustryDataRunEntityCountMetric] = Field(alias="organizations", default=None,)
	people: Optional[IndustryDataIndustryDataRunEntityCountMetric] = Field(alias="people", default=None,)
	unmatchedPeopleByRole: Optional[list[IndustryDataIndustryDataRunRoleCountMetric]] = Field(alias="unmatchedPeopleByRole", default=None,)
	warnings: Optional[int] = Field(alias="warnings", default=None,)

from .industry_data_industry_data_activity_status import IndustryDataIndustryDataActivityStatus
from .industry_data_industry_data_run_entity_count_metric import IndustryDataIndustryDataRunEntityCountMetric
from .industry_data_industry_data_run_role_count_metric import IndustryDataIndustryDataRunRoleCountMetric
from .industry_data_industry_data_run_entity_count_metric import IndustryDataIndustryDataRunEntityCountMetric
from .industry_data_industry_data_run_entity_count_metric import IndustryDataIndustryDataRunEntityCountMetric
from .industry_data_industry_data_run_entity_count_metric import IndustryDataIndustryDataRunEntityCountMetric
from .industry_data_industry_data_run_role_count_metric import IndustryDataIndustryDataRunRoleCountMetric

