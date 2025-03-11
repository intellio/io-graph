from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VerifiedDomain(BaseModel):
	capabilities: Optional[str] = Field(alias="capabilities",default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault",default=None,)
	isInitial: Optional[bool] = Field(alias="isInitial",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	type: Optional[str] = Field(alias="type",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


