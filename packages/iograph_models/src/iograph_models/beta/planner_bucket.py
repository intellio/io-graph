from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerBucket(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	archivalInfo: Optional[PlannerArchivalInfo] = Field(alias="archivalInfo", default=None,)
	creationSource: Optional[Union[PlannerExternalBucketSource]] = Field(alias="creationSource", default=None,discriminator="odata_type", )
	isArchived: Optional[bool] = Field(alias="isArchived", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	orderHint: Optional[str] = Field(alias="orderHint", default=None,)
	planId: Optional[str] = Field(alias="planId", default=None,)
	tasks: Optional[list[Annotated[Union[BusinessScenarioTask]],Field(discriminator="odata_type")]]] = Field(alias="tasks", default=None,)

from .planner_archival_info import PlannerArchivalInfo
from .planner_external_bucket_source import PlannerExternalBucketSource
from .business_scenario_task import BusinessScenarioTask

