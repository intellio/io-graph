from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SubjectRightsRequestEnumeratedMailboxLocation(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	userPrincipalNames: Optional[list[str]] = Field(default=None,alias="userPrincipalNames",)


