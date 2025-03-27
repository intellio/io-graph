from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AppRoleAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.appRoleAssignment"] = Field(alias="@odata.type", default="#microsoft.graph.appRoleAssignment")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	appRoleId: Optional[UUID] = Field(alias="appRoleId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	principalDisplayName: Optional[str] = Field(alias="principalDisplayName", default=None,)
	principalId: Optional[UUID] = Field(alias="principalId", default=None,)
	principalType: Optional[str] = Field(alias="principalType", default=None,)
	resourceDisplayName: Optional[str] = Field(alias="resourceDisplayName", default=None,)
	resourceId: Optional[UUID] = Field(alias="resourceId", default=None,)


