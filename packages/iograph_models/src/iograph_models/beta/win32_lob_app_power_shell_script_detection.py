from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppPowerShellScriptDetection(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	enforceSignatureCheck: Optional[bool] = Field(alias="enforceSignatureCheck",default=None,)
	runAs32Bit: Optional[bool] = Field(alias="runAs32Bit",default=None,)
	scriptContent: Optional[str] = Field(alias="scriptContent",default=None,)


