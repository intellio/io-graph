from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceCustomTaskExtensionCallbackConfiguration(BaseModel):
	timeoutDuration: Optional[str] = Field(default=None,alias="timeoutDuration",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	authorizedApps: list[Application] = Field(alias="authorizedApps",)

from .application import Application

