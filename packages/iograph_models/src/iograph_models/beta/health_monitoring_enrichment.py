from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HealthMonitoringEnrichment(BaseModel):
	impacts: SerializeAsAny[Optional[list[HealthMonitoringResourceImpactSummary]]] = Field(alias="impacts",default=None,)
	state: Optional[HealthMonitoringEnrichmentState | str] = Field(alias="state",default=None,)
	supportingData: Optional[HealthMonitoringSupportingData] = Field(alias="supportingData",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .health_monitoring_resource_impact_summary import HealthMonitoringResourceImpactSummary
from .health_monitoring_enrichment_state import HealthMonitoringEnrichmentState
from .health_monitoring_supporting_data import HealthMonitoringSupportingData

