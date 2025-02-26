from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DelegatedAdminRelationshipRequest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	action: Optional[DelegatedAdminRelationshipRequestAction] = Field(default=None,alias="action",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	status: Optional[DelegatedAdminRelationshipRequestStatus] = Field(default=None,alias="status",)

from .delegated_admin_relationship_request_action import DelegatedAdminRelationshipRequestAction
from .delegated_admin_relationship_request_status import DelegatedAdminRelationshipRequestStatus

