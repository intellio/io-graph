from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessContext(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

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
			if mapping_key == "#microsoft.graph.whatIfApplicationContext":
				from .what_if_application_context import WhatIfApplicationContext
				return WhatIfApplicationContext.model_validate(data)
			if mapping_key == "#microsoft.graph.whatIfAuthenticationContext":
				from .what_if_authentication_context import WhatIfAuthenticationContext
				return WhatIfAuthenticationContext.model_validate(data)
			if mapping_key == "#microsoft.graph.whatIfUserActionContext":
				from .what_if_user_action_context import WhatIfUserActionContext
				return WhatIfUserActionContext.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


