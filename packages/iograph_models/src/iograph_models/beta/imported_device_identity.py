from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class ImportedDeviceIdentity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	enrollmentState: Optional[EnrollmentState | str] = Field(alias="enrollmentState", default=None,)
	importedDeviceIdentifier: Optional[str] = Field(alias="importedDeviceIdentifier", default=None,)
	importedDeviceIdentityType: Optional[ImportedDeviceIdentityType | str] = Field(alias="importedDeviceIdentityType", default=None,)
	lastContactedDateTime: Optional[datetime] = Field(alias="lastContactedDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	platform: Optional[Platform | str] = Field(alias="platform", default=None,)

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
			if mapping_key == "#microsoft.graph.importedDeviceIdentityResult":
				from .imported_device_identity_result import ImportedDeviceIdentityResult
				return ImportedDeviceIdentityResult.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .enrollment_state import EnrollmentState
from .imported_device_identity_type import ImportedDeviceIdentityType
from .platform import Platform
