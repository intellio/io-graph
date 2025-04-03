from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DelegatedAdminRelationshipRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.delegatedAdminRelationshipRequest"] = Field(alias="@odata.type", default="#microsoft.graph.delegatedAdminRelationshipRequest")
	action: Optional[DelegatedAdminRelationshipRequestAction | str] = Field(alias="action", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	status: Optional[DelegatedAdminRelationshipRequestStatus | str] = Field(alias="status", default=None,)

from .delegated_admin_relationship_request_action import DelegatedAdminRelationshipRequestAction
from .delegated_admin_relationship_request_status import DelegatedAdminRelationshipRequestStatus
