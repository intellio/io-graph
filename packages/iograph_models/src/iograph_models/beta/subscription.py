from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class Subscription(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.subscription"] = Field(alias="@odata.type", default="#microsoft.graph.subscription")
	applicationId: Optional[str] = Field(alias="applicationId", default=None,)
	changeType: Optional[str] = Field(alias="changeType", default=None,)
	clientState: Optional[str] = Field(alias="clientState", default=None,)
	creatorId: Optional[str] = Field(alias="creatorId", default=None,)
	encryptionCertificate: Optional[str] = Field(alias="encryptionCertificate", default=None,)
	encryptionCertificateId: Optional[str] = Field(alias="encryptionCertificateId", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	includeResourceData: Optional[bool] = Field(alias="includeResourceData", default=None,)
	latestSupportedTlsVersion: Optional[str] = Field(alias="latestSupportedTlsVersion", default=None,)
	lifecycleNotificationUrl: Optional[str] = Field(alias="lifecycleNotificationUrl", default=None,)
	notificationContentType: Optional[str] = Field(alias="notificationContentType", default=None,)
	notificationQueryOptions: Optional[str] = Field(alias="notificationQueryOptions", default=None,)
	notificationUrl: Optional[str] = Field(alias="notificationUrl", default=None,)
	notificationUrlAppId: Optional[str] = Field(alias="notificationUrlAppId", default=None,)
	resource: Optional[str] = Field(alias="resource", default=None,)

