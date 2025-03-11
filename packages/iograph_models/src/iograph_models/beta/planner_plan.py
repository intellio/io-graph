from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerPlan(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	archivalInfo: Optional[PlannerArchivalInfo] = Field(alias="archivalInfo",default=None,)
	container: SerializeAsAny[Optional[PlannerPlanContainer]] = Field(alias="container",default=None,)
	contexts: Optional[PlannerPlanContextCollection] = Field(alias="contexts",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	creationSource: SerializeAsAny[Optional[PlannerPlanCreation]] = Field(alias="creationSource",default=None,)
	isArchived: Optional[bool] = Field(alias="isArchived",default=None,)
	owner: Optional[str] = Field(alias="owner",default=None,)
	sharedWithContainers: Optional[list[PlannerSharedWithContainer]] = Field(alias="sharedWithContainers",default=None,)
	title: Optional[str] = Field(alias="title",default=None,)
	buckets: Optional[list[PlannerBucket]] = Field(alias="buckets",default=None,)
	details: Optional[PlannerPlanDetails] = Field(alias="details",default=None,)
	tasks: SerializeAsAny[Optional[list[PlannerTask]]] = Field(alias="tasks",default=None,)

from .planner_archival_info import PlannerArchivalInfo
from .planner_plan_container import PlannerPlanContainer
from .planner_plan_context_collection import PlannerPlanContextCollection
from .identity_set import IdentitySet
from .planner_plan_creation import PlannerPlanCreation
from .planner_shared_with_container import PlannerSharedWithContainer
from .planner_bucket import PlannerBucket
from .planner_plan_details import PlannerPlanDetails
from .planner_task import PlannerTask

