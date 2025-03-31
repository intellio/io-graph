from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class NotificationMessageTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.notificationMessageTemplate"] = Field(alias="@odata.type",)
	brandingOptions: Optional[NotificationTemplateBrandingOptions | str] = Field(alias="brandingOptions", default=None,)
	defaultLocale: Optional[str] = Field(alias="defaultLocale", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	localizedNotificationMessages: Optional[list[LocalizedNotificationMessage]] = Field(alias="localizedNotificationMessages", default=None,)

from .notification_template_branding_options import NotificationTemplateBrandingOptions
from .localized_notification_message import LocalizedNotificationMessage
