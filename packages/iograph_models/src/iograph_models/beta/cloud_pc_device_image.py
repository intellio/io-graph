from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class CloudPcDeviceImage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcDeviceImage"] = Field(alias="@odata.type", default="#microsoft.graph.cloudPcDeviceImage")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	errorCode: Optional[CloudPcDeviceImageErrorCode | str] = Field(alias="errorCode", default=None,)
	expirationDate: Optional[str] = Field(alias="expirationDate", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	operatingSystem: Optional[str] = Field(alias="operatingSystem", default=None,)
	osBuildNumber: Optional[str] = Field(alias="osBuildNumber", default=None,)
	osStatus: Optional[CloudPcDeviceImageOsStatus | str] = Field(alias="osStatus", default=None,)
	osVersionNumber: Optional[str] = Field(alias="osVersionNumber", default=None,)
	scopeIds: Optional[list[str]] = Field(alias="scopeIds", default=None,)
	sourceImageResourceId: Optional[str] = Field(alias="sourceImageResourceId", default=None,)
	status: Optional[CloudPcDeviceImageStatus | str] = Field(alias="status", default=None,)
	statusDetails: Optional[CloudPcDeviceImageStatusDetails | str] = Field(alias="statusDetails", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)

from .cloud_pc_device_image_error_code import CloudPcDeviceImageErrorCode
from .cloud_pc_device_image_os_status import CloudPcDeviceImageOsStatus
from .cloud_pc_device_image_status import CloudPcDeviceImageStatus
from .cloud_pc_device_image_status_details import CloudPcDeviceImageStatusDetails
