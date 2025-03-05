from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class StsPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	definition: Optional[list[str]] = Field(default=None,alias="definition",)
	isOrganizationDefault: Optional[bool] = Field(default=None,alias="isOrganizationDefault",)
	appliesTo: Optional[list[DirectoryObject]] = Field(default=None,alias="appliesTo",)

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
			if mapping_key == "#microsoft.graph.activityBasedTimeoutPolicy":
				from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
				return ActivityBasedTimeoutPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.claimsMappingPolicy":
				from .claims_mapping_policy import ClaimsMappingPolicy
				return ClaimsMappingPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.homeRealmDiscoveryPolicy":
				from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
				return HomeRealmDiscoveryPolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.tokenIssuancePolicy":
				from .token_issuance_policy import TokenIssuancePolicy
				return TokenIssuancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.tokenLifetimePolicy":
				from .token_lifetime_policy import TokenLifetimePolicy
				return TokenLifetimePolicy.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .directory_object import DirectoryObject

