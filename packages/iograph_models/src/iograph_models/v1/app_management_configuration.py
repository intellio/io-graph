from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class AppManagementConfiguration(BaseModel):
	keyCredentials: Optional[list[KeyCredentialConfiguration]] = Field(alias="keyCredentials", default=None,)
	passwordCredentials: Optional[list[PasswordCredentialConfiguration]] = Field(alias="passwordCredentials", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

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
			if mapping_key == "#microsoft.graph.appManagementApplicationConfiguration":
				from .app_management_application_configuration import AppManagementApplicationConfiguration
				return AppManagementApplicationConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.appManagementServicePrincipalConfiguration":
				from .app_management_service_principal_configuration import AppManagementServicePrincipalConfiguration
				return AppManagementServicePrincipalConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.customAppManagementConfiguration":
				from .custom_app_management_configuration import CustomAppManagementConfiguration
				return CustomAppManagementConfiguration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .key_credential_configuration import KeyCredentialConfiguration
from .password_credential_configuration import PasswordCredentialConfiguration

