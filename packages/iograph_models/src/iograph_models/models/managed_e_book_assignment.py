from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedEBookAssignment(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	installIntent: Optional[InstallIntent | str] = Field(alias="installIntent",default=None,)
	target: SerializeAsAny[Optional[DeviceAndAppManagementAssignmentTarget]] = Field(alias="target",default=None,)

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
			if mapping_key == "#microsoft.graph.iosVppEBookAssignment":
				from .ios_vpp_e_book_assignment import IosVppEBookAssignment
				return IosVppEBookAssignment.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .install_intent import InstallIntent
from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget

