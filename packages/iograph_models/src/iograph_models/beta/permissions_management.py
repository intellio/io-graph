from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PermissionsManagement(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.permissionsManagement"] = Field(alias="@odata.type", default="#microsoft.graph.permissionsManagement")
	permissionsRequestChanges: Optional[list[PermissionsRequestChange]] = Field(alias="permissionsRequestChanges", default=None,)
	scheduledPermissionsApprovals: Optional[list[Approval]] = Field(alias="scheduledPermissionsApprovals", default=None,)
	scheduledPermissionsRequests: Optional[list[ScheduledPermissionsRequest]] = Field(alias="scheduledPermissionsRequests", default=None,)

from .permissions_request_change import PermissionsRequestChange
from .approval import Approval
from .scheduled_permissions_request import ScheduledPermissionsRequest
