from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows10AssociatedApps(BaseModel):
	appType: Optional[Windows10AppType | str] = Field(alias="appType", default=None,)
	identifier: Optional[str] = Field(alias="identifier", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows10_app_type import Windows10AppType
