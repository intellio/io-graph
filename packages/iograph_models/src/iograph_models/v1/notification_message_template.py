from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class NotificationMessageTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	brandingOptions: Optional[NotificationTemplateBrandingOptions | str] = Field(alias="brandingOptions", default=None,)
	defaultLocale: Optional[str] = Field(alias="defaultLocale", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	localizedNotificationMessages: Optional[list[LocalizedNotificationMessage]] = Field(alias="localizedNotificationMessages", default=None,)

from .notification_template_branding_options import NotificationTemplateBrandingOptions
from .localized_notification_message import LocalizedNotificationMessage

