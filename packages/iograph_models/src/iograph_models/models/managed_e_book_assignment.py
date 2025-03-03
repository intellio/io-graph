from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class ManagedEBookAssignment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	installIntent: Optional[InstallIntent] = Field(default=None,alias="installIntent",)
	target: Optional[DeviceAndAppManagementAssignmentTarget] = Field(default=None,alias="target",)

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

