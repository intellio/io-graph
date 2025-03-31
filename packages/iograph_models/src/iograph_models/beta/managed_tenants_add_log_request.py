from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedTenantsAddLogRequest(BaseModel):
	logInformation: Optional[str] = Field(alias="logInformation", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

