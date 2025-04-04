from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class IdentityUserFlowAttribute(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	dataType: Optional[IdentityUserFlowAttributeDataType | str] = Field(alias="dataType", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	userFlowAttributeType: Optional[IdentityUserFlowAttributeType | str] = Field(alias="userFlowAttributeType", default=None,)

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
