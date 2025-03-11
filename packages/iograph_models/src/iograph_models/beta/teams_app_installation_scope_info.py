from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsAppInstallationScopeInfo(BaseModel):
	scope: Optional[TeamsAppInstallationScopes | str] = Field(alias="scope",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

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
			if mapping_key == "#microsoft.graph.groupChatTeamsAppInstallationScopeInfo":
				from .group_chat_teams_app_installation_scope_info import GroupChatTeamsAppInstallationScopeInfo
				return GroupChatTeamsAppInstallationScopeInfo.model_validate(data)
			if mapping_key == "#microsoft.graph.personalTeamsAppInstallationScopeInfo":
				from .personal_teams_app_installation_scope_info import PersonalTeamsAppInstallationScopeInfo
				return PersonalTeamsAppInstallationScopeInfo.model_validate(data)
			if mapping_key == "#microsoft.graph.teamTeamsAppInstallationScopeInfo":
				from .team_teams_app_installation_scope_info import TeamTeamsAppInstallationScopeInfo
				return TeamTeamsAppInstallationScopeInfo.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .teams_app_installation_scopes import TeamsAppInstallationScopes

