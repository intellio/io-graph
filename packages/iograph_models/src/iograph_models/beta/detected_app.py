from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DetectedApp(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deviceCount: Optional[int] = Field(alias="deviceCount",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	platform: Optional[DetectedAppPlatformType | str] = Field(alias="platform",default=None,)
	publisher: Optional[str] = Field(alias="publisher",default=None,)
	sizeInByte: Optional[int] = Field(alias="sizeInByte",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	managedDevices: SerializeAsAny[Optional[list[ManagedDevice]]] = Field(alias="managedDevices",default=None,)

from .detected_app_platform_type import DetectedAppPlatformType
from .managed_device import ManagedDevice

