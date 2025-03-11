from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedRole(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	assignments: Optional[list[PrivilegedRoleAssignment]] = Field(alias="assignments",default=None,)
	settings: Optional[PrivilegedRoleSettings] = Field(alias="settings",default=None,)
	summary: Optional[PrivilegedRoleSummary] = Field(alias="summary",default=None,)

from .privileged_role_assignment import PrivilegedRoleAssignment
from .privileged_role_settings import PrivilegedRoleSettings
from .privileged_role_summary import PrivilegedRoleSummary

