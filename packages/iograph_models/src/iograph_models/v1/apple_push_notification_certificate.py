from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ApplePushNotificationCertificate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	appleIdentifier: Optional[str] = Field(alias="appleIdentifier", default=None,)
	certificate: Optional[str] = Field(alias="certificate", default=None,)
	certificateSerialNumber: Optional[str] = Field(alias="certificateSerialNumber", default=None,)
	certificateUploadFailureReason: Optional[str] = Field(alias="certificateUploadFailureReason", default=None,)
	certificateUploadStatus: Optional[str] = Field(alias="certificateUploadStatus", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	topicIdentifier: Optional[str] = Field(alias="topicIdentifier", default=None,)


