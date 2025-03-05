from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ChangeNotification(BaseModel):
	changeType: Optional[str | ChangeType] = Field(alias="changeType",default=None,)
	clientState: Optional[str] = Field(alias="clientState",default=None,)
	encryptedContent: Optional[ChangeNotificationEncryptedContent] = Field(alias="encryptedContent",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	lifecycleEvent: Optional[str | LifecycleEventType] = Field(alias="lifecycleEvent",default=None,)
	resource: Optional[str] = Field(alias="resource",default=None,)
	resourceData: Optional[ResourceData] = Field(alias="resourceData",default=None,)
	subscriptionExpirationDateTime: Optional[datetime] = Field(alias="subscriptionExpirationDateTime",default=None,)
	subscriptionId: Optional[UUID] = Field(alias="subscriptionId",default=None,)
	tenantId: Optional[UUID] = Field(alias="tenantId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .change_type import ChangeType
from .change_notification_encrypted_content import ChangeNotificationEncryptedContent
from .lifecycle_event_type import LifecycleEventType
from .resource_data import ResourceData

