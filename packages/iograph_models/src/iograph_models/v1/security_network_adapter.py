from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityNetworkAdapter(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)


