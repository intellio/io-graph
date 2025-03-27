from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppPowerShellScriptDetection(BaseModel):
	odata_type: Literal["#microsoft.graph.win32LobAppPowerShellScriptDetection"] = Field(alias="@odata.type", default="#microsoft.graph.win32LobAppPowerShellScriptDetection")
	enforceSignatureCheck: Optional[bool] = Field(alias="enforceSignatureCheck", default=None,)
	runAs32Bit: Optional[bool] = Field(alias="runAs32Bit", default=None,)
	scriptContent: Optional[str] = Field(alias="scriptContent", default=None,)


