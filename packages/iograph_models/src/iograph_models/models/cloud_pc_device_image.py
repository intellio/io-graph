from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcDeviceImage(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	errorCode: Optional[CloudPcDeviceImageErrorCode] = Field(default=None,alias="errorCode",)
	expirationDate: Optional[str] = Field(default=None,alias="expirationDate",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	operatingSystem: Optional[str] = Field(default=None,alias="operatingSystem",)
	osBuildNumber: Optional[str] = Field(default=None,alias="osBuildNumber",)
	osStatus: Optional[CloudPcDeviceImageOsStatus] = Field(default=None,alias="osStatus",)
	sourceImageResourceId: Optional[str] = Field(default=None,alias="sourceImageResourceId",)
	status: Optional[CloudPcDeviceImageStatus] = Field(default=None,alias="status",)
	version: Optional[str] = Field(default=None,alias="version",)

from .cloud_pc_device_image_error_code import CloudPcDeviceImageErrorCode
from .cloud_pc_device_image_os_status import CloudPcDeviceImageOsStatus
from .cloud_pc_device_image_status import CloudPcDeviceImageStatus

