from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IdentityGovernanceCustomTaskExtensionCallbackConfiguration(BaseModel):
	timeoutDuration: Optional[str] = Field(alias="timeoutDuration", default=None,)
	odata_type: Literal["#microsoft.graph.identityGovernance.customTaskExtensionCallbackConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.identityGovernance.customTaskExtensionCallbackConfiguration")
	authorizedApps: Optional[list[Application]] = Field(alias="authorizedApps", default=None,)

from .application import Application
