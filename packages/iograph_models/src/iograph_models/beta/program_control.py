from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ProgramControl(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.programControl"] = Field(alias="@odata.type", default="#microsoft.graph.programControl")
	controlId: Optional[str] = Field(alias="controlId", default=None,)
	controlTypeId: Optional[str] = Field(alias="controlTypeId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	owner: Optional[Union[AuditUserIdentity]] = Field(alias="owner", default=None,discriminator="odata_type", )
	programId: Optional[str] = Field(alias="programId", default=None,)
	resource: Optional[ProgramResource] = Field(alias="resource", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	program: Optional[Program] = Field(alias="program", default=None,)

from .audit_user_identity import AuditUserIdentity
from .program_resource import ProgramResource
from .program import Program
