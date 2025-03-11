from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class GcpIdentity(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	externalId: Optional[str] = Field(alias="externalId",default=None,)
	source: SerializeAsAny[Optional[AuthorizationSystemIdentitySource]] = Field(alias="source",default=None,)
	authorizationSystem: SerializeAsAny[Optional[AuthorizationSystem]] = Field(alias="authorizationSystem",default=None,)

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
			if mapping_key == "#microsoft.graph.gcpCloudFunction":
				from .gcp_cloud_function import GcpCloudFunction
				return GcpCloudFunction.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpGroup":
				from .gcp_group import GcpGroup
				return GcpGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpServiceAccount":
				from .gcp_service_account import GcpServiceAccount
				return GcpServiceAccount.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpUser":
				from .gcp_user import GcpUser
				return GcpUser.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .authorization_system_identity_source import AuthorizationSystemIdentitySource
from .authorization_system import AuthorizationSystem

