from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConnectPostRequest(BaseModel):
	ownerUserPrincipalName: Optional[str] = Field(alias="ownerUserPrincipalName",default=None,)
	ownerAccessToken: Optional[str] = Field(alias="ownerAccessToken",default=None,)


