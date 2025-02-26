from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field


class TeleconferenceDeviceQuality(BaseModel):
	callChainId: Optional[UUID] = Field(default=None,alias="callChainId",)
	cloudServiceDeploymentEnvironment: Optional[str] = Field(default=None,alias="cloudServiceDeploymentEnvironment",)
	cloudServiceDeploymentId: Optional[str] = Field(default=None,alias="cloudServiceDeploymentId",)
	cloudServiceInstanceName: Optional[str] = Field(default=None,alias="cloudServiceInstanceName",)
	cloudServiceName: Optional[str] = Field(default=None,alias="cloudServiceName",)
	deviceDescription: Optional[str] = Field(default=None,alias="deviceDescription",)
	deviceName: Optional[str] = Field(default=None,alias="deviceName",)
	mediaLegId: Optional[UUID] = Field(default=None,alias="mediaLegId",)
	mediaQualityList: list[TeleconferenceDeviceMediaQuality] = Field(alias="mediaQualityList",)
	participantId: Optional[UUID] = Field(default=None,alias="participantId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .teleconference_device_media_quality import TeleconferenceDeviceMediaQuality

