from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HealthMonitoringAlertConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	emailNotificationConfigurations: Optional[list[HealthMonitoringEmailNotificationConfiguration]] = Field(alias="emailNotificationConfigurations",default=None,)

from .health_monitoring_email_notification_configuration import HealthMonitoringEmailNotificationConfiguration

