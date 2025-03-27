from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class HealthMonitoringEnrichment(BaseModel):
	impacts: Optional[list[Annotated[Union[HealthMonitoringDirectoryObjectImpactSummary, HealthMonitoringApplicationImpactSummary, HealthMonitoringDeviceImpactSummary, HealthMonitoringGroupImpactSummary, HealthMonitoringServicePrincipalImpactSummary, HealthMonitoringUserImpactSummary]],Field(discriminator="odata_type")]]] = Field(alias="impacts", default=None,)
	state: Optional[HealthMonitoringEnrichmentState | str] = Field(alias="state", default=None,)
	supportingData: Optional[HealthMonitoringSupportingData] = Field(alias="supportingData", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .health_monitoring_directory_object_impact_summary import HealthMonitoringDirectoryObjectImpactSummary
from .health_monitoring_application_impact_summary import HealthMonitoringApplicationImpactSummary
from .health_monitoring_device_impact_summary import HealthMonitoringDeviceImpactSummary
from .health_monitoring_group_impact_summary import HealthMonitoringGroupImpactSummary
from .health_monitoring_service_principal_impact_summary import HealthMonitoringServicePrincipalImpactSummary
from .health_monitoring_user_impact_summary import HealthMonitoringUserImpactSummary
from .health_monitoring_enrichment_state import HealthMonitoringEnrichmentState
from .health_monitoring_supporting_data import HealthMonitoringSupportingData

