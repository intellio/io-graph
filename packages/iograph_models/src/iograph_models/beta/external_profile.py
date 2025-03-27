from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.externalProfile"] = Field(alias="@odata.type", default="#microsoft.graph.externalProfile")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	address: Optional[PhysicalOfficeAddress] = Field(alias="address", default=None,)
	companyName: Optional[str] = Field(alias="companyName", default=None,)
	createdBy: Optional[str] = Field(alias="createdBy", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	department: Optional[str] = Field(alias="department", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isDiscoverable: Optional[bool] = Field(alias="isDiscoverable", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	jobTitle: Optional[str] = Field(alias="jobTitle", default=None,)
	phoneNumber: Optional[str] = Field(alias="phoneNumber", default=None,)
	supervisorId: Optional[str] = Field(alias="supervisorId", default=None,)

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
			if mapping_key == "#microsoft.graph.externalUserProfile":
				from .external_user_profile import ExternalUserProfile
				return ExternalUserProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.pendingExternalUserProfile":
				from .pending_external_user_profile import PendingExternalUserProfile
				return PendingExternalUserProfile.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .physical_office_address import PhysicalOfficeAddress

