from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsUserIdentity(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.callRecords.userIdentity"] = Field(alias="@odata.type", default="#microsoft.graph.callRecords.userIdentity")
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)


