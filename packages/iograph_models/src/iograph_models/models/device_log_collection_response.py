from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceLogCollectionResponse(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	enrolledByUser: Optional[str] = Field(default=None,alias="enrolledByUser",)
	expirationDateTimeUTC: Optional[datetime] = Field(default=None,alias="expirationDateTimeUTC",)
	initiatedByUserPrincipalName: Optional[str] = Field(default=None,alias="initiatedByUserPrincipalName",)
	managedDeviceId: Optional[UUID] = Field(default=None,alias="managedDeviceId",)
	receivedDateTimeUTC: Optional[datetime] = Field(default=None,alias="receivedDateTimeUTC",)
	requestedDateTimeUTC: Optional[datetime] = Field(default=None,alias="requestedDateTimeUTC",)
	sizeInKB: Optional[float] | Optional[str] | ReferenceNumeric
	status: Optional[AppLogUploadState] = Field(default=None,alias="status",)

from .reference_numeric import ReferenceNumeric
from .app_log_upload_state import AppLogUploadState

