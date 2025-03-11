from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceAndAppManagementData(BaseModel):
	content: Optional[str] = Field(alias="content",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


