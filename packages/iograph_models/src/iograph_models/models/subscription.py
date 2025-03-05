from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Subscription(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	applicationId: Optional[str] = Field(default=None,alias="applicationId",)
	changeType: Optional[str] = Field(default=None,alias="changeType",)
	clientState: Optional[str] = Field(default=None,alias="clientState",)
	creatorId: Optional[str] = Field(default=None,alias="creatorId",)
	encryptionCertificate: Optional[str] = Field(default=None,alias="encryptionCertificate",)
	encryptionCertificateId: Optional[str] = Field(default=None,alias="encryptionCertificateId",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	includeResourceData: Optional[bool] = Field(default=None,alias="includeResourceData",)
	latestSupportedTlsVersion: Optional[str] = Field(default=None,alias="latestSupportedTlsVersion",)
	lifecycleNotificationUrl: Optional[str] = Field(default=None,alias="lifecycleNotificationUrl",)
	notificationQueryOptions: Optional[str] = Field(default=None,alias="notificationQueryOptions",)
	notificationUrl: Optional[str] = Field(default=None,alias="notificationUrl",)
	notificationUrlAppId: Optional[str] = Field(default=None,alias="notificationUrlAppId",)
	resource: Optional[str] = Field(default=None,alias="resource",)


