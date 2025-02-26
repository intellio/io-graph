from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class SamlOrWsFedProvider(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	issuerUri: Optional[str] = Field(default=None,alias="issuerUri",)
	metadataExchangeUri: Optional[str] = Field(default=None,alias="metadataExchangeUri",)
	passiveSignInUri: Optional[str] = Field(default=None,alias="passiveSignInUri",)
	preferredAuthenticationProtocol: Optional[AuthenticationProtocol] = Field(default=None,alias="preferredAuthenticationProtocol",)
	signingCertificate: Optional[str] = Field(default=None,alias="signingCertificate",)

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
			if mapping_key == "#microsoft.graph.internalDomainFederation":
				from .internal_domain_federation import InternalDomainFederation
				return InternalDomainFederation.model_validate(data)
			if mapping_key == "#microsoft.graph.samlOrWsFedExternalDomainFederation":
				from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
				return SamlOrWsFedExternalDomainFederation.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .authentication_protocol import AuthenticationProtocol

