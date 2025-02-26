from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class TeamsAppInstallation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	consentedPermissionSet: Optional[TeamsAppPermissionSet] = Field(default=None,alias="consentedPermissionSet",)
	teamsApp: Optional[TeamsApp] = Field(default=None,alias="teamsApp",)
	teamsAppDefinition: Optional[TeamsAppDefinition] = Field(default=None,alias="teamsAppDefinition",)

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
			if mapping_key == "#microsoft.graph.userScopeTeamsAppInstallation":
				from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation
				return UserScopeTeamsAppInstallation.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .teams_app_permission_set import TeamsAppPermissionSet
from .teams_app import TeamsApp
from .teams_app_definition import TeamsAppDefinition

