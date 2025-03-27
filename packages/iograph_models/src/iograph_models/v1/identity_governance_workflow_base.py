from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceWorkflowBase(BaseModel):
	category: Optional[IdentityGovernanceLifecycleWorkflowCategory | str] = Field(alias="category", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	executionConditions: Optional[Union[IdentityGovernanceOnDemandExecutionOnly, IdentityGovernanceTriggerAndScopeBasedConditions]] = Field(alias="executionConditions", default=None,discriminator="odata_type", )
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	isSchedulingEnabled: Optional[bool] = Field(alias="isSchedulingEnabled", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	createdBy: Optional[User] = Field(alias="createdBy", default=None,)
	lastModifiedBy: Optional[User] = Field(alias="lastModifiedBy", default=None,)
	tasks: Optional[list[IdentityGovernanceTask]] = Field(alias="tasks", default=None,)
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
from .identity_governance_on_demand_execution_only import IdentityGovernanceOnDemandExecutionOnly
from .identity_governance_trigger_and_scope_based_conditions import IdentityGovernanceTriggerAndScopeBasedConditions
from .user import User
from .user import User
from .identity_governance_task import IdentityGovernanceTask

