from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Request(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	approvalId: Optional[str] = Field(default=None,alias="approvalId",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	customData: Optional[str] = Field(default=None,alias="customData",)
	status: Optional[str] = Field(default=None,alias="status",)

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
			if mapping_key == "#microsoft.graph.privilegedAccessScheduleRequest":
				from .privileged_access_schedule_request import PrivilegedAccessScheduleRequest
				return PrivilegedAccessScheduleRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedAccessGroupAssignmentScheduleRequest":
				from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
				return PrivilegedAccessGroupAssignmentScheduleRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedAccessGroupEligibilityScheduleRequest":
				from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
				return PrivilegedAccessGroupEligibilityScheduleRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleAssignmentScheduleRequest":
				from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest
				return UnifiedRoleAssignmentScheduleRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleEligibilityScheduleRequest":
				from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest
				return UnifiedRoleEligibilityScheduleRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.userConsentRequest":
				from .user_consent_request import UserConsentRequest
				return UserConsentRequest.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_set import IdentitySet

