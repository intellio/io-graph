from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceHealthScriptRemediationSummary(BaseModel):
	remediatedDeviceCount: Optional[int] = Field(alias="remediatedDeviceCount",default=None,)
	scriptCount: Optional[int] = Field(alias="scriptCount",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


