from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcDisasterRecoveryNetworkSetting(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

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
			if mapping_key == "#microsoft.graph.cloudPcDisasterRecoveryAzureConnectionSetting":
				from .cloud_pc_disaster_recovery_azure_connection_setting import CloudPcDisasterRecoveryAzureConnectionSetting
				return CloudPcDisasterRecoveryAzureConnectionSetting.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcDisasterRecoveryMicrosoftHostedNetworkSetting":
				from .cloud_pc_disaster_recovery_microsoft_hosted_network_setting import CloudPcDisasterRecoveryMicrosoftHostedNetworkSetting
				return CloudPcDisasterRecoveryMicrosoftHostedNetworkSetting.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


