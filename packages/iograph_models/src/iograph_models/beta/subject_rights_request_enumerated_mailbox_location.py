from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SubjectRightsRequestEnumeratedMailboxLocation(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	upns: Optional[list[str]] = Field(alias="upns",default=None,)
	userPrincipalNames: Optional[list[str]] = Field(alias="userPrincipalNames",default=None,)


