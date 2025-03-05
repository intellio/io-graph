from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsInformationProtectionResourceCollection(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	resources: Optional[list[str]] = Field(default=None,alias="resources",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


