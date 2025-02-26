from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class InvitationRedemptionIdentityProviderConfiguration(BaseModel):
	fallbackIdentityProvider: Optional[B2bIdentityProvidersType] = Field(default=None,alias="fallbackIdentityProvider",)
	primaryIdentityProviderPrecedenceOrder: Optional[B2bIdentityProvidersType] = Field(default=None,alias="primaryIdentityProviderPrecedenceOrder",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

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
			if mapping_key == "#microsoft.graph.defaultInvitationRedemptionIdentityProviderConfiguration":
				from .default_invitation_redemption_identity_provider_configuration import DefaultInvitationRedemptionIdentityProviderConfiguration
				return DefaultInvitationRedemptionIdentityProviderConfiguration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .b2b_identity_providers_type import B2bIdentityProvidersType
from .b2b_identity_providers_type import B2bIdentityProvidersType

