from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsMinimumOperatingSystem(BaseModel):
	v10_0: Optional[bool] = Field(default=None,alias="v10_0",)
	v8_0: Optional[bool] = Field(default=None,alias="v8_0",)
	v8_1: Optional[bool] = Field(default=None,alias="v8_1",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


