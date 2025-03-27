from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PermissionsManagement(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	permissionsRequestChanges: Optional[list[PermissionsRequestChange]] = Field(alias="permissionsRequestChanges", default=None,)
	scheduledPermissionsApprovals: Optional[list[Approval]] = Field(alias="scheduledPermissionsApprovals", default=None,)
	scheduledPermissionsRequests: Optional[list[ScheduledPermissionsRequest]] = Field(alias="scheduledPermissionsRequests", default=None,)

from .permissions_request_change import PermissionsRequestChange
from .approval import Approval
from .scheduled_permissions_request import ScheduledPermissionsRequest

