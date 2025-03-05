from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleScheduleBase(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appScopeId: Optional[str] = Field(default=None,alias="appScopeId",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	createdUsing: Optional[str] = Field(default=None,alias="createdUsing",)
	directoryScopeId: Optional[str] = Field(default=None,alias="directoryScopeId",)
	modifiedDateTime: Optional[datetime] = Field(default=None,alias="modifiedDateTime",)
	principalId: Optional[str] = Field(default=None,alias="principalId",)
	roleDefinitionId: Optional[str] = Field(default=None,alias="roleDefinitionId",)
	status: Optional[str] = Field(default=None,alias="status",)
	appScope: Optional[AppScope] = Field(default=None,alias="appScope",)
	directoryScope: SerializeAsAny[Optional[DirectoryObject]] = Field(default=None,alias="directoryScope",)
	principal: SerializeAsAny[Optional[DirectoryObject]] = Field(default=None,alias="principal",)
	roleDefinition: Optional[UnifiedRoleDefinition] = Field(default=None,alias="roleDefinition",)

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
			if mapping_key == "#microsoft.graph.unifiedRoleAssignmentSchedule":
				from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
				return UnifiedRoleAssignmentSchedule.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleEligibilitySchedule":
				from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
				return UnifiedRoleEligibilitySchedule.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .app_scope import AppScope
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .unified_role_definition import UnifiedRoleDefinition

