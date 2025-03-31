from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class AuthenticationEventListener(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	authenticationEventsFlowId: Optional[str] = Field(alias="authenticationEventsFlowId", default=None,)
	conditions: Optional[AuthenticationConditions] = Field(alias="conditions", default=None,)

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
			if mapping_key == "#microsoft.graph.onAttributeCollectionListener":
				from .on_attribute_collection_listener import OnAttributeCollectionListener
				return OnAttributeCollectionListener.model_validate(data)
			if mapping_key == "#microsoft.graph.onAuthenticationMethodLoadStartListener":
				from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener
				return OnAuthenticationMethodLoadStartListener.model_validate(data)
			if mapping_key == "#microsoft.graph.onInteractiveAuthFlowStartListener":
				from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener
				return OnInteractiveAuthFlowStartListener.model_validate(data)
			if mapping_key == "#microsoft.graph.onTokenIssuanceStartListener":
				from .on_token_issuance_start_listener import OnTokenIssuanceStartListener
				return OnTokenIssuanceStartListener.model_validate(data)
			if mapping_key == "#microsoft.graph.onUserCreateStartListener":
				from .on_user_create_start_listener import OnUserCreateStartListener
				return OnUserCreateStartListener.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .authentication_conditions import AuthenticationConditions
