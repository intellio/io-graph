from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PlannerPlanConfigurationBucketLocalizationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PlannerPlanConfigurationBucketLocalization]] = Field(alias="value", default=None,)

from .planner_plan_configuration_bucket_localization import PlannerPlanConfigurationBucketLocalization
