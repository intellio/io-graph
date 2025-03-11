from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceLogCollectionResponse(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	enrolledByUser: Optional[str] = Field(alias="enrolledByUser",default=None,)
	errorCode: Optional[int] = Field(alias="errorCode",default=None,)
	expirationDateTimeUTC: Optional[datetime] = Field(alias="expirationDateTimeUTC",default=None,)
	initiatedByUserPrincipalName: Optional[str] = Field(alias="initiatedByUserPrincipalName",default=None,)
	managedDeviceId: Optional[UUID] = Field(alias="managedDeviceId",default=None,)
	receivedDateTimeUTC: Optional[datetime] = Field(alias="receivedDateTimeUTC",default=None,)
	requestedDateTimeUTC: Optional[datetime] = Field(alias="requestedDateTimeUTC",default=None,)
	size: float | str | ReferenceNumeric
	sizeInKB: float | str | ReferenceNumeric
	status: Optional[AppLogUploadState | str] = Field(alias="status",default=None,)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .app_log_upload_state import AppLogUploadState

