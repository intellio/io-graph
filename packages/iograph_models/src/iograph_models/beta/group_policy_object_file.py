from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyObjectFile(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	content: Optional[str] = Field(alias="content",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	groupPolicyObjectId: Optional[UUID] = Field(alias="groupPolicyObjectId",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	ouDistinguishedName: Optional[str] = Field(alias="ouDistinguishedName",default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds",default=None,)


