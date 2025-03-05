from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsUserIdentity(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)


