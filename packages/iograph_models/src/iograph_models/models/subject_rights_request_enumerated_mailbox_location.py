from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SubjectRightsRequestEnumeratedMailboxLocation(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	userPrincipalNames: list[Optional[str]] = Field(alias="userPrincipalNames",)


