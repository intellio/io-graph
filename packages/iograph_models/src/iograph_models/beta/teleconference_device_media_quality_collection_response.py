from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeleconferenceDeviceMediaQualityCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[TeleconferenceDeviceMediaQuality]]] = Field(alias="value",default=None,)

from .teleconference_device_media_quality import TeleconferenceDeviceMediaQuality

