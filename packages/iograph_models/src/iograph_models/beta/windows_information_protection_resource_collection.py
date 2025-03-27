from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsInformationProtectionResourceCollection(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	resources: Optional[list[str]] = Field(alias="resources", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


