from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ClaimsMapping(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	email: Optional[str] = Field(alias="email",default=None,)
	givenName: Optional[str] = Field(alias="givenName",default=None,)
	surname: Optional[str] = Field(alias="surname",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


