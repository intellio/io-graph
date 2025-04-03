from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ApplePushNotificationCertificate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.applePushNotificationCertificate"] = Field(alias="@odata.type", default="#microsoft.graph.applePushNotificationCertificate")
	appleIdentifier: Optional[str] = Field(alias="appleIdentifier", default=None,)
	certificate: Optional[str] = Field(alias="certificate", default=None,)
	certificateSerialNumber: Optional[str] = Field(alias="certificateSerialNumber", default=None,)
	certificateUploadFailureReason: Optional[str] = Field(alias="certificateUploadFailureReason", default=None,)
	certificateUploadStatus: Optional[str] = Field(alias="certificateUploadStatus", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	topicIdentifier: Optional[str] = Field(alias="topicIdentifier", default=None,)

