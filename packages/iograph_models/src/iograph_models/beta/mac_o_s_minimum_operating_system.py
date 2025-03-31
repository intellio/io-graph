from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MacOSMinimumOperatingSystem(BaseModel):
	v10_10: Optional[bool] = Field(alias="v10_10", default=None,)
	v10_11: Optional[bool] = Field(alias="v10_11", default=None,)
	v10_12: Optional[bool] = Field(alias="v10_12", default=None,)
	v10_13: Optional[bool] = Field(alias="v10_13", default=None,)
	v10_14: Optional[bool] = Field(alias="v10_14", default=None,)
	v10_15: Optional[bool] = Field(alias="v10_15", default=None,)
	v10_7: Optional[bool] = Field(alias="v10_7", default=None,)
	v10_8: Optional[bool] = Field(alias="v10_8", default=None,)
	v10_9: Optional[bool] = Field(alias="v10_9", default=None,)
	v11_0: Optional[bool] = Field(alias="v11_0", default=None,)
	v12_0: Optional[bool] = Field(alias="v12_0", default=None,)
	v13_0: Optional[bool] = Field(alias="v13_0", default=None,)
	v14_0: Optional[bool] = Field(alias="v14_0", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

