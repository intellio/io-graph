from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CommunicationsApplicationIdentity(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	applicationType: Optional[str] = Field(alias="applicationType",default=None,)
	hidden: Optional[bool] = Field(alias="hidden",default=None,)


