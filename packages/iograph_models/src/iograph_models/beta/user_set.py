from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class UserSet(BaseModel):
	isBackup: Optional[bool] = Field(alias="isBackup", default=None,)
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
			if mapping_key == "#microsoft.graph.connectedOrganizationMembers":
				from .connected_organization_members import ConnectedOrganizationMembers
				return ConnectedOrganizationMembers.model_validate(data)
			if mapping_key == "#microsoft.graph.externalSponsors":
				from .external_sponsors import ExternalSponsors
				return ExternalSponsors.model_validate(data)
			if mapping_key == "#microsoft.graph.groupMembers":
				from .group_members import GroupMembers
				return GroupMembers.model_validate(data)
			if mapping_key == "#microsoft.graph.internalSponsors":
				from .internal_sponsors import InternalSponsors
				return InternalSponsors.model_validate(data)
			if mapping_key == "#microsoft.graph.requestorManager":
				from .requestor_manager import RequestorManager
				return RequestorManager.model_validate(data)
			if mapping_key == "#microsoft.graph.singleUser":
				from .single_user import SingleUser
				return SingleUser.model_validate(data)
			if mapping_key == "#microsoft.graph.targetUserSponsors":
				from .target_user_sponsors import TargetUserSponsors
				return TargetUserSponsors.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

