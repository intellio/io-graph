from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RolesAssignedOutsidePrivilegedIdentityManagementAlertIncidentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident]] = Field(alias="value", default=None,)

from .roles_assigned_outside_privileged_identity_management_alert_incident import RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident
