from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DelegatedAdminAccessAssignment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	accessContainer: Optional[DelegatedAdminAccessContainer] = Field(default=None,alias="accessContainer",)
	accessDetails: Optional[DelegatedAdminAccessDetails] = Field(default=None,alias="accessDetails",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	status: Optional[DelegatedAdminAccessAssignmentStatus] = Field(default=None,alias="status",)

from .delegated_admin_access_container import DelegatedAdminAccessContainer
from .delegated_admin_access_details import DelegatedAdminAccessDetails
from .delegated_admin_access_assignment_status import DelegatedAdminAccessAssignmentStatus

