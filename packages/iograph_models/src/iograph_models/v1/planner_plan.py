from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerPlan(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	container: Optional[PlannerPlanContainer] = Field(alias="container", default=None,)
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	owner: Optional[str] = Field(alias="owner", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	buckets: Optional[list[PlannerBucket]] = Field(alias="buckets", default=None,)
	details: Optional[PlannerPlanDetails] = Field(alias="details", default=None,)
	tasks: Optional[list[PlannerTask]] = Field(alias="tasks", default=None,)

from .planner_plan_container import PlannerPlanContainer
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .planner_bucket import PlannerBucket
from .planner_plan_details import PlannerPlanDetails
from .planner_task import PlannerTask

