from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class SamlOrWsFedProvider(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	issuerUri: Optional[str] = Field(alias="issuerUri",default=None,)
	metadataExchangeUri: Optional[str] = Field(alias="metadataExchangeUri",default=None,)
	passiveSignInUri: Optional[str] = Field(alias="passiveSignInUri",default=None,)
	preferredAuthenticationProtocol: Optional[AuthenticationProtocol | str] = Field(alias="preferredAuthenticationProtocol",default=None,)
	signingCertificate: Optional[str] = Field(alias="signingCertificate",default=None,)

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

