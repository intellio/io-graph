from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EBookInstallSummary(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	failedDeviceCount: Optional[int] = Field(default=None,alias="failedDeviceCount",)
	failedUserCount: Optional[int] = Field(default=None,alias="failedUserCount",)
	installedDeviceCount: Optional[int] = Field(default=None,alias="installedDeviceCount",)
	installedUserCount: Optional[int] = Field(default=None,alias="installedUserCount",)
	notInstalledDeviceCount: Optional[int] = Field(default=None,alias="notInstalledDeviceCount",)
	notInstalledUserCount: Optional[int] = Field(default=None,alias="notInstalledUserCount",)


