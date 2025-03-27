from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class PreApprovedPermissions(BaseModel):
	permissionKind: Optional[PermissionKind | str] = Field(alias="permissionKind", default=None,)
	permissionType: Optional[PermissionType | str] = Field(alias="permissionType", default=None,)
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
			if mapping_key == "#microsoft.graph.allPreApprovedPermissions":
				from .all_pre_approved_permissions import AllPreApprovedPermissions
				return AllPreApprovedPermissions.model_validate(data)
			if mapping_key == "#microsoft.graph.allPreApprovedPermissionsOnResourceApp":
				from .all_pre_approved_permissions_on_resource_app import AllPreApprovedPermissionsOnResourceApp
				return AllPreApprovedPermissionsOnResourceApp.model_validate(data)
			if mapping_key == "#microsoft.graph.enumeratedPreApprovedPermissions":
				from .enumerated_pre_approved_permissions import EnumeratedPreApprovedPermissions
				return EnumeratedPreApprovedPermissions.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .permission_kind import PermissionKind
from .permission_type import PermissionType

