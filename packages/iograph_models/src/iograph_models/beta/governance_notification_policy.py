from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GovernanceNotificationPolicy(BaseModel):
	enabledTemplateTypes: Optional[list[str]] = Field(alias="enabledTemplateTypes",default=None,)
	notificationTemplates: Optional[list[GovernanceNotificationTemplate]] = Field(alias="notificationTemplates",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .governance_notification_template import GovernanceNotificationTemplate

