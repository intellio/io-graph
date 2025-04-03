from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceLogCollectionResponse(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceLogCollectionResponse"] = Field(alias="@odata.type", default="#microsoft.graph.deviceLogCollectionResponse")
	enrolledByUser: Optional[str] = Field(alias="enrolledByUser", default=None,)
	expirationDateTimeUTC: Optional[datetime] = Field(alias="expirationDateTimeUTC", default=None,)
	initiatedByUserPrincipalName: Optional[str] = Field(alias="initiatedByUserPrincipalName", default=None,)
	managedDeviceId: Optional[UUID] = Field(alias="managedDeviceId", default=None,)
	receivedDateTimeUTC: Optional[datetime] = Field(alias="receivedDateTimeUTC", default=None,)
	requestedDateTimeUTC: Optional[datetime] = Field(alias="requestedDateTimeUTC", default=None,)
	sizeInKB: float | str | ReferenceNumeric
	status: Optional[AppLogUploadState | str] = Field(alias="status", default=None,)

from .reference_numeric import ReferenceNumeric
from .app_log_upload_state import AppLogUploadState
