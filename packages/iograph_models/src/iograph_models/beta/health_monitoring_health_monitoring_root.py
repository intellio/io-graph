from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HealthMonitoringHealthMonitoringRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	alertConfigurations: Optional[list[HealthMonitoringAlertConfiguration]] = Field(alias="alertConfigurations", default=None,)
	alerts: Optional[list[HealthMonitoringAlert]] = Field(alias="alerts", default=None,)

from .health_monitoring_alert_configuration import HealthMonitoringAlertConfiguration
from .health_monitoring_alert import HealthMonitoringAlert

