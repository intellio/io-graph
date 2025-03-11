from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerRelationshipBasedUserType(BaseModel):
	roleKind: Optional[PlannerUserRoleKind | str] = Field(alias="roleKind",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	role: Optional[PlannerRelationshipUserRoles | str] = Field(alias="role",default=None,)

from .planner_user_role_kind import PlannerUserRoleKind
from .planner_relationship_user_roles import PlannerRelationshipUserRoles

