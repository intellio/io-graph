from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class ConditionalAccessPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	conditions: Optional[ConditionalAccessConditionSet] = Field(alias="conditions", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	grantControls: Optional[ConditionalAccessGrantControls] = Field(alias="grantControls", default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime", default=None,)
	sessionControls: Optional[ConditionalAccessSessionControls] = Field(alias="sessionControls", default=None,)
	state: Optional[ConditionalAccessPolicyState | str] = Field(alias="state", default=None,)

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
			if mapping_key == "#microsoft.graph.conditionalAccessWhatIfPolicy":
				from .conditional_access_what_if_policy import ConditionalAccessWhatIfPolicy
				return ConditionalAccessWhatIfPolicy.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .conditional_access_condition_set import ConditionalAccessConditionSet
from .conditional_access_grant_controls import ConditionalAccessGrantControls
from .conditional_access_session_controls import ConditionalAccessSessionControls
from .conditional_access_policy_state import ConditionalAccessPolicyState
