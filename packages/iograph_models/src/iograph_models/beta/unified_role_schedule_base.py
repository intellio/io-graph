from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleScheduleBase(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appScopeId: Optional[str] = Field(alias="appScopeId",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	createdUsing: Optional[str] = Field(alias="createdUsing",default=None,)
	directoryScopeId: Optional[str] = Field(alias="directoryScopeId",default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime",default=None,)
	principalId: Optional[str] = Field(alias="principalId",default=None,)
	roleDefinitionId: Optional[str] = Field(alias="roleDefinitionId",default=None,)
	status: Optional[str] = Field(alias="status",default=None,)
	appScope: SerializeAsAny[Optional[AppScope]] = Field(alias="appScope",default=None,)
	directoryScope: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="directoryScope",default=None,)
	principal: SerializeAsAny[Optional[DirectoryObject]] = Field(alias="principal",default=None,)
	roleDefinition: Optional[UnifiedRoleDefinition] = Field(alias="roleDefinition",default=None,)

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

