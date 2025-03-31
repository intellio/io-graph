from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class TeamworkDevice(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.teamworkDevice"] = Field(alias="@odata.type",)
	activityState: Optional[TeamworkDeviceActivityState | str] = Field(alias="activityState", default=None,)
	companyAssetTag: Optional[str] = Field(alias="companyAssetTag", default=None,)
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	currentUser: Optional[TeamworkUserIdentity] = Field(alias="currentUser", default=None,)
	deviceType: Optional[TeamworkDeviceType | str] = Field(alias="deviceType", default=None,)
	hardwareDetail: Optional[TeamworkHardwareDetail] = Field(alias="hardwareDetail", default=None,)
	healthStatus: Optional[TeamworkDeviceHealthStatus | str] = Field(alias="healthStatus", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	notes: Optional[str] = Field(alias="notes", default=None,)
	activity: Optional[TeamworkDeviceActivity] = Field(alias="activity", default=None,)
	configuration: Optional[TeamworkDeviceConfiguration] = Field(alias="configuration", default=None,)
	health: Optional[TeamworkDeviceHealth] = Field(alias="health", default=None,)
	operations: Optional[list[TeamworkDeviceOperation]] = Field(alias="operations", default=None,)

from .teamwork_device_activity_state import TeamworkDeviceActivityState
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .teamwork_user_identity import TeamworkUserIdentity
from .teamwork_device_type import TeamworkDeviceType
from .teamwork_hardware_detail import TeamworkHardwareDetail
from .teamwork_device_health_status import TeamworkDeviceHealthStatus
from .teamwork_device_activity import TeamworkDeviceActivity
from .teamwork_device_configuration import TeamworkDeviceConfiguration
from .teamwork_device_health import TeamworkDeviceHealth
from .teamwork_device_operation import TeamworkDeviceOperation
