from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class IdentityUserFlow(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	userFlowType: Optional[UserFlowType | str] = Field(alias="userFlowType", default=None,)
	userFlowTypeVersion: float | str | ReferenceNumeric

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
			if mapping_key == "#microsoft.graph.b2cIdentityUserFlow":
				from .b2c_identity_user_flow import B2cIdentityUserFlow
				return B2cIdentityUserFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.b2xIdentityUserFlow":
				from .b2x_identity_user_flow import B2xIdentityUserFlow
				return B2xIdentityUserFlow.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .user_flow_type import UserFlowType
from .reference_numeric import ReferenceNumeric
