from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceCustomTaskExtensionCallbackConfiguration(BaseModel):
	timeoutDuration: Optional[str] = Field(alias="timeoutDuration",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	authorizedApps: Optional[list[Application]] = Field(alias="authorizedApps",default=None,)

from .application import Application

