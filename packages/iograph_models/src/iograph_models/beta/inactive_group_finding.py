from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class InactiveGroupFinding(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	actionSummary: Optional[ActionSummary] = Field(alias="actionSummary",default=None,)
	permissionsCreepIndex: Optional[PermissionsCreepIndex] = Field(alias="permissionsCreepIndex",default=None,)
	group: SerializeAsAny[Optional[AuthorizationSystemIdentity]] = Field(alias="group",default=None,)

from .action_summary import ActionSummary
from .permissions_creep_index import PermissionsCreepIndex
from .authorization_system_identity import AuthorizationSystemIdentity

