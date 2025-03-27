from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class EncryptContent(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	odata_type: Literal["#microsoft.graph.encryptContent"] = Field(alias="@odata.type", default="#microsoft.graph.encryptContent")
	encryptWith: Optional[EncryptWith | str] = Field(alias="encryptWith", default=None,)

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
			if mapping_key == "#microsoft.graph.encryptWithTemplate":
				from .encrypt_with_template import EncryptWithTemplate
				return EncryptWithTemplate.model_validate(data)
			if mapping_key == "#microsoft.graph.encryptWithUserDefinedRights":
				from .encrypt_with_user_defined_rights import EncryptWithUserDefinedRights
				return EncryptWithUserDefinedRights.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .encrypt_with import EncryptWith

