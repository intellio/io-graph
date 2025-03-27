from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class HealthMonitoringAlert(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	alertType: Optional[HealthMonitoringAlertType | str] = Field(alias="alertType", default=None,)
	category: Optional[HealthMonitoringCategory | str] = Field(alias="category", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	documentation: Optional[HealthMonitoringDocumentation] = Field(alias="documentation", default=None,)
	enrichment: Optional[HealthMonitoringEnrichment] = Field(alias="enrichment", default=None,)
	scenario: Optional[HealthMonitoringScenario | str] = Field(alias="scenario", default=None,)
	signals: Optional[HealthMonitoringSignals] = Field(alias="signals", default=None,)
	state: Optional[HealthMonitoringAlertState | str] = Field(alias="state", default=None,)

from .health_monitoring_alert_type import HealthMonitoringAlertType
from .health_monitoring_category import HealthMonitoringCategory
from .health_monitoring_documentation import HealthMonitoringDocumentation
from .health_monitoring_enrichment import HealthMonitoringEnrichment
from .health_monitoring_scenario import HealthMonitoringScenario
from .health_monitoring_signals import HealthMonitoringSignals
from .health_monitoring_alert_state import HealthMonitoringAlertState

