from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosMinimumOperatingSystem(BaseModel):
	v10_0: Optional[bool] = Field(alias="v10_0", default=None,)
	v11_0: Optional[bool] = Field(alias="v11_0", default=None,)
	v12_0: Optional[bool] = Field(alias="v12_0", default=None,)
	v13_0: Optional[bool] = Field(alias="v13_0", default=None,)
	v14_0: Optional[bool] = Field(alias="v14_0", default=None,)
	v15_0: Optional[bool] = Field(alias="v15_0", default=None,)
	v16_0: Optional[bool] = Field(alias="v16_0", default=None,)
	v17_0: Optional[bool] = Field(alias="v17_0", default=None,)
	v8_0: Optional[bool] = Field(alias="v8_0", default=None,)
	v9_0: Optional[bool] = Field(alias="v9_0", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

