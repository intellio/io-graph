from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PlannerRelationshipBasedUserType(BaseModel):
	roleKind: Optional[PlannerUserRoleKind | str] = Field(alias="roleKind", default=None,)
	odata_type: Literal["#microsoft.graph.plannerRelationshipBasedUserType"] = Field(alias="@odata.type", default="#microsoft.graph.plannerRelationshipBasedUserType")
	role: Optional[PlannerRelationshipUserRoles | str] = Field(alias="role", default=None,)

from .planner_user_role_kind import PlannerUserRoleKind
from .planner_relationship_user_roles import PlannerRelationshipUserRoles
