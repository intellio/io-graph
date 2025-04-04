from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class HealthMonitoringEmailNotificationConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[HealthMonitoringEmailNotificationConfiguration]] = Field(alias="value", default=None,)

from .health_monitoring_email_notification_configuration import HealthMonitoringEmailNotificationConfiguration
