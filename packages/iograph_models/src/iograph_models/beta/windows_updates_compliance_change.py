from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class WindowsUpdatesComplianceChange(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	isRevoked: Optional[bool] = Field(alias="isRevoked", default=None,)
	revokedDateTime: Optional[datetime] = Field(alias="revokedDateTime", default=None,)
	updatePolicy: Optional[WindowsUpdatesUpdatePolicy] = Field(alias="updatePolicy", default=None,)

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
			if mapping_key == "#microsoft.graph.windowsUpdates.contentApproval":
				from .windows_updates_content_approval import WindowsUpdatesContentApproval
				return WindowsUpdatesContentApproval.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .windows_updates_update_policy import WindowsUpdatesUpdatePolicy
