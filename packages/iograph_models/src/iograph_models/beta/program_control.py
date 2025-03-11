from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ProgramControl(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	controlId: Optional[str] = Field(alias="controlId",default=None,)
	controlTypeId: Optional[str] = Field(alias="controlTypeId",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	owner: SerializeAsAny[Optional[UserIdentity]] = Field(alias="owner",default=None,)
	programId: Optional[str] = Field(alias="programId",default=None,)
	resource: Optional[ProgramResource] = Field(alias="resource",default=None,)
	status: Optional[str] = Field(alias="status",default=None,)
	program: Optional[Program] = Field(alias="program",default=None,)

from .user_identity import UserIdentity
from .program_resource import ProgramResource
from .program import Program

