from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class HealthMonitoringDirectoryObjectImpactSummary(BaseModel):
	impactedCount: Optional[str] = Field(alias="impactedCount",default=None,)
	impactedCountLimitExceeded: Optional[bool] = Field(alias="impactedCountLimitExceeded",default=None,)
	resourceType: Optional[str] = Field(alias="resourceType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	resourceSampling: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="resourceSampling",default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.healthMonitoring.applicationImpactSummary":
				from .health_monitoring_application_impact_summary import HealthMonitoringApplicationImpactSummary
				return HealthMonitoringApplicationImpactSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.healthMonitoring.deviceImpactSummary":
				from .health_monitoring_device_impact_summary import HealthMonitoringDeviceImpactSummary
				return HealthMonitoringDeviceImpactSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.healthMonitoring.groupImpactSummary":
				from .health_monitoring_group_impact_summary import HealthMonitoringGroupImpactSummary
				return HealthMonitoringGroupImpactSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.healthMonitoring.servicePrincipalImpactSummary":
				from .health_monitoring_service_principal_impact_summary import HealthMonitoringServicePrincipalImpactSummary
				return HealthMonitoringServicePrincipalImpactSummary.model_validate(data)
			if mapping_key == "#microsoft.graph.healthMonitoring.userImpactSummary":
				from .health_monitoring_user_impact_summary import HealthMonitoringUserImpactSummary
				return HealthMonitoringUserImpactSummary.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .directory_object import DirectoryObject

