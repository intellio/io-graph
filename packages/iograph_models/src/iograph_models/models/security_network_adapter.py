from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityNetworkAdapter(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	name: Optional[str] = Field(default=None,alias="name",)


