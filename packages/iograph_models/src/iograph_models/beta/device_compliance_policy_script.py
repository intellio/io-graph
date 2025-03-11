from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceCompliancePolicyScript(BaseModel):
	deviceComplianceScriptId: Optional[str] = Field(alias="deviceComplianceScriptId",default=None,)
	rulesContent: Optional[str] = Field(alias="rulesContent",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


