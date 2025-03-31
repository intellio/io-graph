from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TenantSetupInfo(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.tenantSetupInfo"] = Field(alias="@odata.type",)
	firstTimeSetup: Optional[bool] = Field(alias="firstTimeSetup", default=None,)
	relevantRolesSettings: Optional[list[str]] = Field(alias="relevantRolesSettings", default=None,)
	setupStatus: Optional[SetupStatus | str] = Field(alias="setupStatus", default=None,)
	skipSetup: Optional[bool] = Field(alias="skipSetup", default=None,)
	userRolesActions: Optional[str] = Field(alias="userRolesActions", default=None,)
	defaultRolesSettings: Optional[PrivilegedRoleSettings] = Field(alias="defaultRolesSettings", default=None,)

from .setup_status import SetupStatus
from .privileged_role_settings import PrivilegedRoleSettings
