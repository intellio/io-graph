from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SubjectRightsRequestEnumeratedMailboxLocation(BaseModel):
	odata_type: Literal["#microsoft.graph.subjectRightsRequestEnumeratedMailboxLocation"] = Field(alias="@odata.type", default="#microsoft.graph.subjectRightsRequestEnumeratedMailboxLocation")
	upns: Optional[list[str]] = Field(alias="upns", default=None,)
	userPrincipalNames: Optional[list[str]] = Field(alias="userPrincipalNames", default=None,)

