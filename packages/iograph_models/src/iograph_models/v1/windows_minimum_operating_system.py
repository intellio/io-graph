from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsMinimumOperatingSystem(BaseModel):
	v10_0: Optional[bool] = Field(alias="v10_0", default=None,)
	v8_0: Optional[bool] = Field(alias="v8_0", default=None,)
	v8_1: Optional[bool] = Field(alias="v8_1", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

