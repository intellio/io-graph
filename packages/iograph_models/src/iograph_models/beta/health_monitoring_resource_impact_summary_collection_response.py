from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class HealthMonitoringResourceImpactSummaryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[HealthMonitoringDirectoryObjectImpactSummary, HealthMonitoringApplicationImpactSummary, HealthMonitoringDeviceImpactSummary, HealthMonitoringGroupImpactSummary, HealthMonitoringServicePrincipalImpactSummary, HealthMonitoringUserImpactSummary]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .health_monitoring_directory_object_impact_summary import HealthMonitoringDirectoryObjectImpactSummary
from .health_monitoring_application_impact_summary import HealthMonitoringApplicationImpactSummary
from .health_monitoring_device_impact_summary import HealthMonitoringDeviceImpactSummary
from .health_monitoring_group_impact_summary import HealthMonitoringGroupImpactSummary
from .health_monitoring_service_principal_impact_summary import HealthMonitoringServicePrincipalImpactSummary
from .health_monitoring_user_impact_summary import HealthMonitoringUserImpactSummary

