from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VerifiedDomain(BaseModel):
	capabilities: Optional[str] = Field(default=None,alias="capabilities",)
	isDefault: Optional[bool] = Field(default=None,alias="isDefault",)
	isInitial: Optional[bool] = Field(default=None,alias="isInitial",)
	name: Optional[str] = Field(default=None,alias="name",)
	type: Optional[str] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


