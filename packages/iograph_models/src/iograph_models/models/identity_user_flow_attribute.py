from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class IdentityUserFlowAttribute(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	dataType: Optional[IdentityUserFlowAttributeDataType] = Field(default=None,alias="dataType",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	userFlowAttributeType: Optional[IdentityUserFlowAttributeType] = Field(default=None,alias="userFlowAttributeType",)

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
			if mapping_key == "#microsoft.graph.identityBuiltInUserFlowAttribute":
				from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute
				return IdentityBuiltInUserFlowAttribute.model_validate(data)
			if mapping_key == "#microsoft.graph.identityCustomUserFlowAttribute":
				from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute
				return IdentityCustomUserFlowAttribute.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_user_flow_attribute_data_type import IdentityUserFlowAttributeDataType
from .identity_user_flow_attribute_type import IdentityUserFlowAttributeType

