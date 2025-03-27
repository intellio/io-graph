from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ImportedAppleDeviceIdentity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	discoverySource: Optional[DiscoverySource | str] = Field(alias="discoverySource", default=None,)
	enrollmentState: Optional[EnrollmentState | str] = Field(alias="enrollmentState", default=None,)
	isDeleted: Optional[bool] = Field(alias="isDeleted", default=None,)
	isSupervised: Optional[bool] = Field(alias="isSupervised", default=None,)
	lastContactedDateTime: Optional[datetime] = Field(alias="lastContactedDateTime", default=None,)
	platform: Optional[Platform | str] = Field(alias="platform", default=None,)
	requestedEnrollmentProfileAssignmentDateTime: Optional[datetime] = Field(alias="requestedEnrollmentProfileAssignmentDateTime", default=None,)
	requestedEnrollmentProfileId: Optional[str] = Field(alias="requestedEnrollmentProfileId", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)

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
			if mapping_key == "#microsoft.graph.importedAppleDeviceIdentityResult":
				from .imported_apple_device_identity_result import ImportedAppleDeviceIdentityResult
				return ImportedAppleDeviceIdentityResult.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .discovery_source import DiscoverySource
from .enrollment_state import EnrollmentState
from .platform import Platform

