from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class TeamInfo(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)
	team: Optional[Team] = Field(default=None,alias="team",)

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
			if mapping_key == "#microsoft.graph.associatedTeamInfo":
				from .associated_team_info import AssociatedTeamInfo
				return AssociatedTeamInfo.model_validate(data)
			if mapping_key == "#microsoft.graph.sharedWithChannelTeamInfo":
				from .shared_with_channel_team_info import SharedWithChannelTeamInfo
				return SharedWithChannelTeamInfo.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .team import Team

