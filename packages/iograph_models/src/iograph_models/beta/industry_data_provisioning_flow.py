from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataProvisioningFlow(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	readinessStatus: Optional[IndustryDataReadinessStatus | str] = Field(alias="readinessStatus",default=None,)

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
			if mapping_key == "#microsoft.graph.industryData.administrativeUnitProvisioningFlow":
				from .industry_data_administrative_unit_provisioning_flow import IndustryDataAdministrativeUnitProvisioningFlow
				return IndustryDataAdministrativeUnitProvisioningFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.classGroupProvisioningFlow":
				from .industry_data_class_group_provisioning_flow import IndustryDataClassGroupProvisioningFlow
				return IndustryDataClassGroupProvisioningFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.securityGroupProvisioningFlow":
				from .industry_data_security_group_provisioning_flow import IndustryDataSecurityGroupProvisioningFlow
				return IndustryDataSecurityGroupProvisioningFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.userProvisioningFlow":
				from .industry_data_user_provisioning_flow import IndustryDataUserProvisioningFlow
				return IndustryDataUserProvisioningFlow.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .industry_data_readiness_status import IndustryDataReadinessStatus

