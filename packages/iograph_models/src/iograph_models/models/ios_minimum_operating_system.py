from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosMinimumOperatingSystem(BaseModel):
	v10_0: Optional[bool] = Field(default=None,alias="v10_0",)
	v11_0: Optional[bool] = Field(default=None,alias="v11_0",)
	v12_0: Optional[bool] = Field(default=None,alias="v12_0",)
	v13_0: Optional[bool] = Field(default=None,alias="v13_0",)
	v14_0: Optional[bool] = Field(default=None,alias="v14_0",)
	v15_0: Optional[bool] = Field(default=None,alias="v15_0",)
	v8_0: Optional[bool] = Field(default=None,alias="v8_0",)
	v9_0: Optional[bool] = Field(default=None,alias="v9_0",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


