from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class TeamworkDeviceConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.teamworkDeviceConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.teamworkDeviceConfiguration")
	cameraConfiguration: Optional[TeamworkCameraConfiguration] = Field(alias="cameraConfiguration", default=None,)
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayConfiguration: Optional[TeamworkDisplayConfiguration] = Field(alias="displayConfiguration", default=None,)
	hardwareConfiguration: Optional[TeamworkHardwareConfiguration] = Field(alias="hardwareConfiguration", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	microphoneConfiguration: Optional[TeamworkMicrophoneConfiguration] = Field(alias="microphoneConfiguration", default=None,)
	softwareVersions: Optional[TeamworkDeviceSoftwareVersions] = Field(alias="softwareVersions", default=None,)
	speakerConfiguration: Optional[TeamworkSpeakerConfiguration] = Field(alias="speakerConfiguration", default=None,)
	systemConfiguration: Optional[TeamworkSystemConfiguration] = Field(alias="systemConfiguration", default=None,)
	teamsClientConfiguration: Optional[TeamworkTeamsClientConfiguration] = Field(alias="teamsClientConfiguration", default=None,)

from .teamwork_camera_configuration import TeamworkCameraConfiguration
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .teamwork_display_configuration import TeamworkDisplayConfiguration
from .teamwork_hardware_configuration import TeamworkHardwareConfiguration
from .teamwork_microphone_configuration import TeamworkMicrophoneConfiguration
from .teamwork_device_software_versions import TeamworkDeviceSoftwareVersions
from .teamwork_speaker_configuration import TeamworkSpeakerConfiguration
from .teamwork_system_configuration import TeamworkSystemConfiguration
from .teamwork_teams_client_configuration import TeamworkTeamsClientConfiguration
