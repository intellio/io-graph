from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class PlannerPlan(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.plannerPlan"] = Field(alias="@odata.type", default="#microsoft.graph.plannerPlan")
	archivalInfo: Optional[PlannerArchivalInfo] = Field(alias="archivalInfo", default=None,)
	container: Optional[Union[PlannerSharedWithContainer]] = Field(alias="container", default=None,discriminator="odata_type", )
	contexts: Optional[PlannerPlanContextCollection] = Field(alias="contexts", default=None,)
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	creationSource: Optional[Union[PlannerExternalPlanSource]] = Field(alias="creationSource", default=None,discriminator="odata_type", )
	isArchived: Optional[bool] = Field(alias="isArchived", default=None,)
	owner: Optional[str] = Field(alias="owner", default=None,)
	sharedWithContainers: Optional[list[PlannerSharedWithContainer]] = Field(alias="sharedWithContainers", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	buckets: Optional[list[PlannerBucket]] = Field(alias="buckets", default=None,)
	details: Optional[PlannerPlanDetails] = Field(alias="details", default=None,)
	tasks: Optional[list[Annotated[Union[BusinessScenarioTask],Field(discriminator="odata_type")]]] = Field(alias="tasks", default=None,)

from .planner_archival_info import PlannerArchivalInfo
from .planner_shared_with_container import PlannerSharedWithContainer
from .planner_plan_context_collection import PlannerPlanContextCollection
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .planner_external_plan_source import PlannerExternalPlanSource
from .planner_bucket import PlannerBucket
from .planner_plan_details import PlannerPlanDetails
from .business_scenario_task import BusinessScenarioTask
