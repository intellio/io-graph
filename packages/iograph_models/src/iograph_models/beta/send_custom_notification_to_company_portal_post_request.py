from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Send_custom_notification_to_company_portalPostRequest(BaseModel):
	notificationTitle: Optional[str] = Field(alias="notificationTitle", default=None,)
	notificationBody: Optional[str] = Field(alias="notificationBody", default=None,)


