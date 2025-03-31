from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsMinimumOperatingSystem(BaseModel):
	v10_0: Optional[bool] = Field(alias="v10_0", default=None,)
	v10_1607: Optional[bool] = Field(alias="v10_1607", default=None,)
	v10_1703: Optional[bool] = Field(alias="v10_1703", default=None,)
	v10_1709: Optional[bool] = Field(alias="v10_1709", default=None,)
	v10_1803: Optional[bool] = Field(alias="v10_1803", default=None,)
	v10_1809: Optional[bool] = Field(alias="v10_1809", default=None,)
	v10_1903: Optional[bool] = Field(alias="v10_1903", default=None,)
	v10_1909: Optional[bool] = Field(alias="v10_1909", default=None,)
	v10_2004: Optional[bool] = Field(alias="v10_2004", default=None,)
	v10_21H1: Optional[bool] = Field(alias="v10_21H1", default=None,)
	v10_2H20: Optional[bool] = Field(alias="v10_2H20", default=None,)
	v8_0: Optional[bool] = Field(alias="v8_0", default=None,)
	v8_1: Optional[bool] = Field(alias="v8_1", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

