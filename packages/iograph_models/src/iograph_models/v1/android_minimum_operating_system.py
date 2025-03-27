from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidMinimumOperatingSystem(BaseModel):
	v10_0: Optional[bool] = Field(alias="v10_0", default=None,)
	v11_0: Optional[bool] = Field(alias="v11_0", default=None,)
	v4_0: Optional[bool] = Field(alias="v4_0", default=None,)
	v4_0_3: Optional[bool] = Field(alias="v4_0_3", default=None,)
	v4_1: Optional[bool] = Field(alias="v4_1", default=None,)
	v4_2: Optional[bool] = Field(alias="v4_2", default=None,)
	v4_3: Optional[bool] = Field(alias="v4_3", default=None,)
	v4_4: Optional[bool] = Field(alias="v4_4", default=None,)
	v5_0: Optional[bool] = Field(alias="v5_0", default=None,)
	v5_1: Optional[bool] = Field(alias="v5_1", default=None,)
	v6_0: Optional[bool] = Field(alias="v6_0", default=None,)
	v7_0: Optional[bool] = Field(alias="v7_0", default=None,)
	v7_1: Optional[bool] = Field(alias="v7_1", default=None,)
	v8_0: Optional[bool] = Field(alias="v8_0", default=None,)
	v8_1: Optional[bool] = Field(alias="v8_1", default=None,)
	v9_0: Optional[bool] = Field(alias="v9_0", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


