from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class UnifiedRoleScheduleInstanceBase(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appScopeId: Optional[str] = Field(default=None,alias="appScopeId",)
	directoryScopeId: Optional[str] = Field(default=None,alias="directoryScopeId",)
	principalId: Optional[str] = Field(default=None,alias="principalId",)
	roleDefinitionId: Optional[str] = Field(default=None,alias="roleDefinitionId",)
	appScope: Optional[AppScope] = Field(default=None,alias="appScope",)
	directoryScope: Optional[DirectoryObject] = Field(default=None,alias="directoryScope",)
	principal: Optional[DirectoryObject] = Field(default=None,alias="principal",)
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
			if mapping_key == "#microsoft.graph.unifiedRoleAssignmentScheduleInstance":
				from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance
				return UnifiedRoleAssignmentScheduleInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleEligibilityScheduleInstance":
				from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance
				return UnifiedRoleEligibilityScheduleInstance.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .app_scope import AppScope
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject
from .unified_role_definition import UnifiedRoleDefinition

