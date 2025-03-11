from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkDeviceConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	cameraConfiguration: Optional[TeamworkCameraConfiguration] = Field(alias="cameraConfiguration",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayConfiguration: Optional[TeamworkDisplayConfiguration] = Field(alias="displayConfiguration",default=None,)
	hardwareConfiguration: Optional[TeamworkHardwareConfiguration] = Field(alias="hardwareConfiguration",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	microphoneConfiguration: Optional[TeamworkMicrophoneConfiguration] = Field(alias="microphoneConfiguration",default=None,)
	softwareVersions: Optional[TeamworkDeviceSoftwareVersions] = Field(alias="softwareVersions",default=None,)
	speakerConfiguration: Optional[TeamworkSpeakerConfiguration] = Field(alias="speakerConfiguration",default=None,)
	systemConfiguration: Optional[TeamworkSystemConfiguration] = Field(alias="systemConfiguration",default=None,)
	teamsClientConfiguration: Optional[TeamworkTeamsClientConfiguration] = Field(alias="teamsClientConfiguration",default=None,)

from .teamwork_camera_configuration import TeamworkCameraConfiguration
from .identity_set import IdentitySet
from .teamwork_display_configuration import TeamworkDisplayConfiguration
from .teamwork_hardware_configuration import TeamworkHardwareConfiguration
from .identity_set import IdentitySet
from .teamwork_microphone_configuration import TeamworkMicrophoneConfiguration
from .teamwork_device_software_versions import TeamworkDeviceSoftwareVersions
from .teamwork_speaker_configuration import TeamworkSpeakerConfiguration
from .teamwork_system_configuration import TeamworkSystemConfiguration
from .teamwork_teams_client_configuration import TeamworkTeamsClientConfiguration

