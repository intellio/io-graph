from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcConnectionSettings(BaseModel):
	enableSingleSignOn: Optional[bool] = Field(alias="enableSingleSignOn", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

