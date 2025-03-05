from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ChangeNotification(BaseModel):
	changeType: Optional[ChangeType] = Field(default=None,alias="changeType",)
	clientState: Optional[str] = Field(default=None,alias="clientState",)
	encryptedContent: Optional[ChangeNotificationEncryptedContent] = Field(default=None,alias="encryptedContent",)
	id: Optional[str] = Field(default=None,alias="id",)
	lifecycleEvent: Optional[LifecycleEventType] = Field(default=None,alias="lifecycleEvent",)
	resource: Optional[str] = Field(default=None,alias="resource",)
	resourceData: Optional[ResourceData] = Field(default=None,alias="resourceData",)
	subscriptionExpirationDateTime: Optional[datetime] = Field(default=None,alias="subscriptionExpirationDateTime",)
	subscriptionId: Optional[UUID] = Field(default=None,alias="subscriptionId",)
	tenantId: Optional[UUID] = Field(default=None,alias="tenantId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .change_type import ChangeType
from .change_notification_encrypted_content import ChangeNotificationEncryptedContent
from .lifecycle_event_type import LifecycleEventType
from .resource_data import ResourceData

