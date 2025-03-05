from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class IdentitySource(BaseModel):
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
			if mapping_key == "#microsoft.graph.azureActiveDirectoryTenant":
				from .azure_active_directory_tenant import AzureActiveDirectoryTenant
				return AzureActiveDirectoryTenant.model_validate(data)
			if mapping_key == "#microsoft.graph.crossCloudAzureActiveDirectoryTenant":
				from .cross_cloud_azure_active_directory_tenant import CrossCloudAzureActiveDirectoryTenant
				return CrossCloudAzureActiveDirectoryTenant.model_validate(data)
			if mapping_key == "#microsoft.graph.domainIdentitySource":
				from .domain_identity_source import DomainIdentitySource
				return DomainIdentitySource.model_validate(data)
			if mapping_key == "#microsoft.graph.externalDomainFederation":
				from .external_domain_federation import ExternalDomainFederation
				return ExternalDomainFederation.model_validate(data)
			if mapping_key == "#microsoft.graph.socialIdentitySource":
				from .social_identity_source import SocialIdentitySource
				return SocialIdentitySource.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


