from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class HealthMonitoringAlertConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.healthMonitoring.alertConfiguration"] = Field(alias="@odata.type",)
	emailNotificationConfigurations: Optional[list[HealthMonitoringEmailNotificationConfiguration]] = Field(alias="emailNotificationConfigurations", default=None,)

from .health_monitoring_email_notification_configuration import HealthMonitoringEmailNotificationConfiguration
