from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerTaskRoleBasedRule(BaseModel):
	defaultRule: Optional[str] = Field(alias="defaultRule",default=None,)
	propertyRule: Optional[PlannerTaskPropertyRule] = Field(alias="propertyRule",default=None,)
	role: SerializeAsAny[Optional[PlannerTaskConfigurationRoleBase]] = Field(alias="role",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .planner_task_property_rule import PlannerTaskPropertyRule
from .planner_task_configuration_role_base import PlannerTaskConfigurationRoleBase

