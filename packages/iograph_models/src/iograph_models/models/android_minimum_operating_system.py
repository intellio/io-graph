from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AndroidMinimumOperatingSystem(BaseModel):
	v10_0: Optional[bool] = Field(default=None,alias="v10_0",)
	v11_0: Optional[bool] = Field(default=None,alias="v11_0",)
	v4_0: Optional[bool] = Field(default=None,alias="v4_0",)
	v4_0_3: Optional[bool] = Field(default=None,alias="v4_0_3",)
	v4_1: Optional[bool] = Field(default=None,alias="v4_1",)
	v4_2: Optional[bool] = Field(default=None,alias="v4_2",)
	v4_3: Optional[bool] = Field(default=None,alias="v4_3",)
	v4_4: Optional[bool] = Field(default=None,alias="v4_4",)
	v5_0: Optional[bool] = Field(default=None,alias="v5_0",)
	v5_1: Optional[bool] = Field(default=None,alias="v5_1",)
	v6_0: Optional[bool] = Field(default=None,alias="v6_0",)
	v7_0: Optional[bool] = Field(default=None,alias="v7_0",)
	v7_1: Optional[bool] = Field(default=None,alias="v7_1",)
	v8_0: Optional[bool] = Field(default=None,alias="v8_0",)
	v8_1: Optional[bool] = Field(default=None,alias="v8_1",)
	v9_0: Optional[bool] = Field(default=None,alias="v9_0",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


