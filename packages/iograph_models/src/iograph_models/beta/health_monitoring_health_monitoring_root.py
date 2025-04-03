from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class HealthMonitoringHealthMonitoringRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.healthMonitoring.healthMonitoringRoot"] = Field(alias="@odata.type", default="#microsoft.graph.healthMonitoring.healthMonitoringRoot")
	alertConfigurations: Optional[list[HealthMonitoringAlertConfiguration]] = Field(alias="alertConfigurations", default=None,)
	alerts: Optional[list[HealthMonitoringAlert]] = Field(alias="alerts", default=None,)

from .health_monitoring_alert_configuration import HealthMonitoringAlertConfiguration
from .health_monitoring_alert import HealthMonitoringAlert
