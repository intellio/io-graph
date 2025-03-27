from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class TeleconferenceDeviceQuality(BaseModel):
	callChainId: Optional[UUID] = Field(alias="callChainId", default=None,)
	cloudServiceDeploymentEnvironment: Optional[str] = Field(alias="cloudServiceDeploymentEnvironment", default=None,)
	cloudServiceDeploymentId: Optional[str] = Field(alias="cloudServiceDeploymentId", default=None,)
	cloudServiceInstanceName: Optional[str] = Field(alias="cloudServiceInstanceName", default=None,)
	cloudServiceName: Optional[str] = Field(alias="cloudServiceName", default=None,)
	deviceDescription: Optional[str] = Field(alias="deviceDescription", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	mediaLegId: Optional[UUID] = Field(alias="mediaLegId", default=None,)
	mediaQualityList: Optional[list[Annotated[Union[TeleconferenceDeviceAudioQuality, TeleconferenceDeviceVideoQuality, TeleconferenceDeviceScreenSharingQuality]],Field(discriminator="odata_type")]]] = Field(alias="mediaQualityList", default=None,)
	participantId: Optional[UUID] = Field(alias="participantId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .teleconference_device_audio_quality import TeleconferenceDeviceAudioQuality
from .teleconference_device_video_quality import TeleconferenceDeviceVideoQuality
from .teleconference_device_screen_sharing_quality import TeleconferenceDeviceScreenSharingQuality

