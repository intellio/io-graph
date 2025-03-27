from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class TeleconferenceDeviceMediaQualityCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[TeleconferenceDeviceAudioQuality, TeleconferenceDeviceVideoQuality, TeleconferenceDeviceScreenSharingQuality],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .teleconference_device_audio_quality import TeleconferenceDeviceAudioQuality
from .teleconference_device_video_quality import TeleconferenceDeviceVideoQuality
from .teleconference_device_screen_sharing_quality import TeleconferenceDeviceScreenSharingQuality

