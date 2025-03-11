from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DelegatedAdminRelationshipRequest(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	action: Optional[DelegatedAdminRelationshipRequestAction | str] = Field(alias="action",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	status: Optional[DelegatedAdminRelationshipRequestStatus | str] = Field(alias="status",default=None,)

from .delegated_admin_relationship_request_action import DelegatedAdminRelationshipRequestAction
from .delegated_admin_relationship_request_status import DelegatedAdminRelationshipRequestStatus

