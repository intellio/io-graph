from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceWorkflowBase(BaseModel):
	category: Optional[IdentityGovernanceLifecycleWorkflowCategory] = Field(default=None,alias="category",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	executionConditions: SerializeAsAny[Optional[IdentityGovernanceWorkflowExecutionConditions]] = Field(default=None,alias="executionConditions",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	isSchedulingEnabled: Optional[bool] = Field(default=None,alias="isSchedulingEnabled",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	createdBy: Optional[User] = Field(default=None,alias="createdBy",)
	lastModifiedBy: Optional[User] = Field(default=None,alias="lastModifiedBy",)
	tasks: Optional[list[IdentityGovernanceTask]] = Field(default=None,alias="tasks",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

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
			if mapping_key == "#microsoft.graph.identityGovernance.workflow":
				from .identity_governance_workflow import IdentityGovernanceWorkflow
				return IdentityGovernanceWorkflow.model_validate(data)
			if mapping_key == "#microsoft.graph.identityGovernance.workflowVersion":
				from .identity_governance_workflow_version import IdentityGovernanceWorkflowVersion
				return IdentityGovernanceWorkflowVersion.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_governance_lifecycle_workflow_category import IdentityGovernanceLifecycleWorkflowCategory
from .identity_governance_workflow_execution_conditions import IdentityGovernanceWorkflowExecutionConditions
from .user import User
from .user import User
from .identity_governance_task import IdentityGovernanceTask

