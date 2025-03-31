from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class UserIdentity(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userIdentity"] = Field(alias="@odata.type", default="#microsoft.graph.userIdentity")
	ipAddress: Optional[str] = Field(alias="ipAddress", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

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
			if mapping_key == "#microsoft.graph.auditUserIdentity":
				from .audit_user_identity import AuditUserIdentity
				return AuditUserIdentity.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

