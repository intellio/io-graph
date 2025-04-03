from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class GroupPolicyObjectFile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.groupPolicyObjectFile"] = Field(alias="@odata.type", default="#microsoft.graph.groupPolicyObjectFile")
	content: Optional[str] = Field(alias="content", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	groupPolicyObjectId: Optional[UUID] = Field(alias="groupPolicyObjectId", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	ouDistinguishedName: Optional[str] = Field(alias="ouDistinguishedName", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)

