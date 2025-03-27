from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerTaskRoleBasedRule(BaseModel):
	defaultRule: Optional[str] = Field(alias="defaultRule", default=None,)
	propertyRule: Optional[PlannerTaskPropertyRule] = Field(alias="propertyRule", default=None,)
	role: Optional[Union[PlannerRelationshipBasedUserType]] = Field(alias="role", default=None,discriminator="odata_type", )
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .planner_task_property_rule import PlannerTaskPropertyRule
from .planner_relationship_based_user_type import PlannerRelationshipBasedUserType

