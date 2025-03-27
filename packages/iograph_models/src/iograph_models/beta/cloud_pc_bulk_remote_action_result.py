from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcBulkRemoteActionResult(BaseModel):
	failedDeviceIds: Optional[list[str]] = Field(alias="failedDeviceIds", default=None,)
	notFoundDeviceIds: Optional[list[str]] = Field(alias="notFoundDeviceIds", default=None,)
	notSupportedDeviceIds: Optional[list[str]] = Field(alias="notSupportedDeviceIds", default=None,)
	successfulDeviceIds: Optional[list[str]] = Field(alias="successfulDeviceIds", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


