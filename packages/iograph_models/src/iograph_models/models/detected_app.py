from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DetectedApp(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deviceCount: Optional[int] = Field(default=None,alias="deviceCount",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	platform: Optional[DetectedAppPlatformType] = Field(default=None,alias="platform",)
	publisher: Optional[str] = Field(default=None,alias="publisher",)
	sizeInByte: Optional[int] = Field(default=None,alias="sizeInByte",)
	version: Optional[str] = Field(default=None,alias="version",)
	managedDevices: Optional[list[ManagedDevice]] = Field(default=None,alias="managedDevices",)

from .detected_app_platform_type import DetectedAppPlatformType
from .managed_device import ManagedDevice

