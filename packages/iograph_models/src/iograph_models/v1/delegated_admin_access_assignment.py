from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DelegatedAdminAccessAssignment(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	accessContainer: Optional[DelegatedAdminAccessContainer] = Field(alias="accessContainer",default=None,)
	accessDetails: Optional[DelegatedAdminAccessDetails] = Field(alias="accessDetails",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	status: Optional[DelegatedAdminAccessAssignmentStatus | str] = Field(alias="status",default=None,)

from .delegated_admin_access_container import DelegatedAdminAccessContainer
from .delegated_admin_access_details import DelegatedAdminAccessDetails
from .delegated_admin_access_assignment_status import DelegatedAdminAccessAssignmentStatus

