from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class NotificationMessageTemplate(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	brandingOptions: Optional[NotificationTemplateBrandingOptions] = Field(default=None,alias="brandingOptions",)
	defaultLocale: Optional[str] = Field(default=None,alias="defaultLocale",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	roleScopeTagIds: list[Optional[str]] = Field(alias="roleScopeTagIds",)
	localizedNotificationMessages: list[LocalizedNotificationMessage] = Field(alias="localizedNotificationMessages",)

from .notification_template_branding_options import NotificationTemplateBrandingOptions
from .localized_notification_message import LocalizedNotificationMessage

