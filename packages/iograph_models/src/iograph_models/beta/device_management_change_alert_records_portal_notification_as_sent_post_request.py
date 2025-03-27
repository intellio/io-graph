from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Device_management_change_alert_records_portal_notification_as_sentPostRequest(BaseModel):
	alertRecordIds: Optional[list[str]] = Field(alias="alertRecordIds", default=None,)


