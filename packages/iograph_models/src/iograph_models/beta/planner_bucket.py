from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerBucket(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	archivalInfo: Optional[PlannerArchivalInfo] = Field(alias="archivalInfo",default=None,)
	creationSource: SerializeAsAny[Optional[PlannerBucketCreation]] = Field(alias="creationSource",default=None,)
	isArchived: Optional[bool] = Field(alias="isArchived",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	orderHint: Optional[str] = Field(alias="orderHint",default=None,)
	planId: Optional[str] = Field(alias="planId",default=None,)
	tasks: SerializeAsAny[Optional[list[PlannerTask]]] = Field(alias="tasks",default=None,)

from .planner_archival_info import PlannerArchivalInfo
from .planner_bucket_creation import PlannerBucketCreation
from .planner_task import PlannerTask

