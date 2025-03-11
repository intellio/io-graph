from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeleconferenceDeviceQuality(BaseModel):
	callChainId: Optional[UUID] = Field(alias="callChainId",default=None,)
	cloudServiceDeploymentEnvironment: Optional[str] = Field(alias="cloudServiceDeploymentEnvironment",default=None,)
	cloudServiceDeploymentId: Optional[str] = Field(alias="cloudServiceDeploymentId",default=None,)
	cloudServiceInstanceName: Optional[str] = Field(alias="cloudServiceInstanceName",default=None,)
	cloudServiceName: Optional[str] = Field(alias="cloudServiceName",default=None,)
	deviceDescription: Optional[str] = Field(alias="deviceDescription",default=None,)
	deviceName: Optional[str] = Field(alias="deviceName",default=None,)
	mediaLegId: Optional[UUID] = Field(alias="mediaLegId",default=None,)
	mediaQualityList: SerializeAsAny[Optional[list[TeleconferenceDeviceMediaQuality]]] = Field(alias="mediaQualityList",default=None,)
	participantId: Optional[UUID] = Field(alias="participantId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .teleconference_device_media_quality import TeleconferenceDeviceMediaQuality

