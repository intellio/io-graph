from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PlannerPlanConfigurationLocalization(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.plannerPlanConfigurationLocalization"] = Field(alias="@odata.type", default="#microsoft.graph.plannerPlanConfigurationLocalization")
	buckets: Optional[list[PlannerPlanConfigurationBucketLocalization]] = Field(alias="buckets", default=None,)
	languageTag: Optional[str] = Field(alias="languageTag", default=None,)
	planTitle: Optional[str] = Field(alias="planTitle", default=None,)

from .planner_plan_configuration_bucket_localization import PlannerPlanConfigurationBucketLocalization
