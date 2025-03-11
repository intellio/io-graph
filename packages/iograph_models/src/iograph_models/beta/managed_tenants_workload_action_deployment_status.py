from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsWorkloadActionDeploymentStatus(BaseModel):
	actionId: Optional[str] = Field(alias="actionId",default=None,)
	deployedPolicyId: Optional[str] = Field(alias="deployedPolicyId",default=None,)
	error: SerializeAsAny[Optional[GenericError]] = Field(alias="error",default=None,)
	excludeGroups: Optional[list[str]] = Field(alias="excludeGroups",default=None,)
	includeAllUsers: Optional[bool] = Field(alias="includeAllUsers",default=None,)
	includeGroups: Optional[list[str]] = Field(alias="includeGroups",default=None,)
	lastDeploymentDateTime: Optional[datetime] = Field(alias="lastDeploymentDateTime",default=None,)
	status: Optional[ManagedTenantsWorkloadActionStatus | str] = Field(alias="status",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .generic_error import GenericError
from .managed_tenants_workload_action_status import ManagedTenantsWorkloadActionStatus

