from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DelegatedAdminAccessAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.delegatedAdminAccessAssignment"] = Field(alias="@odata.type", default="#microsoft.graph.delegatedAdminAccessAssignment")
	accessContainer: Optional[DelegatedAdminAccessContainer] = Field(alias="accessContainer", default=None,)
	accessDetails: Optional[DelegatedAdminAccessDetails] = Field(alias="accessDetails", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	status: Optional[DelegatedAdminAccessAssignmentStatus | str] = Field(alias="status", default=None,)

from .delegated_admin_access_container import DelegatedAdminAccessContainer
from .delegated_admin_access_details import DelegatedAdminAccessDetails
from .delegated_admin_access_assignment_status import DelegatedAdminAccessAssignmentStatus
