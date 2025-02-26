from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ApplePushNotificationCertificate(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appleIdentifier: Optional[str] = Field(default=None,alias="appleIdentifier",)
	certificate: Optional[str] = Field(default=None,alias="certificate",)
	certificateSerialNumber: Optional[str] = Field(default=None,alias="certificateSerialNumber",)
	certificateUploadFailureReason: Optional[str] = Field(default=None,alias="certificateUploadFailureReason",)
	certificateUploadStatus: Optional[str] = Field(default=None,alias="certificateUploadStatus",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	topicIdentifier: Optional[str] = Field(default=None,alias="topicIdentifier",)


