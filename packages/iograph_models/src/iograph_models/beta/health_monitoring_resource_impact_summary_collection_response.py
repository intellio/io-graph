from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HealthMonitoringResourceImpactSummaryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[HealthMonitoringResourceImpactSummary]]] = Field(alias="value",default=None,)

from .health_monitoring_resource_impact_summary import HealthMonitoringResourceImpactSummary

