from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class HealthMonitoringAlertConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[HealthMonitoringAlertConfiguration]] = Field(alias="value", default=None,)

from .health_monitoring_alert_configuration import HealthMonitoringAlertConfiguration
