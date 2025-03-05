from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MacOSMinimumOperatingSystem(BaseModel):
	v10_10: Optional[bool] = Field(default=None,alias="v10_10",)
	v10_11: Optional[bool] = Field(default=None,alias="v10_11",)
	v10_12: Optional[bool] = Field(default=None,alias="v10_12",)
	v10_13: Optional[bool] = Field(default=None,alias="v10_13",)
	v10_14: Optional[bool] = Field(default=None,alias="v10_14",)
	v10_15: Optional[bool] = Field(default=None,alias="v10_15",)
	v10_7: Optional[bool] = Field(default=None,alias="v10_7",)
	v10_8: Optional[bool] = Field(default=None,alias="v10_8",)
	v10_9: Optional[bool] = Field(default=None,alias="v10_9",)
	v11_0: Optional[bool] = Field(default=None,alias="v11_0",)
	v12_0: Optional[bool] = Field(default=None,alias="v12_0",)
	v13_0: Optional[bool] = Field(default=None,alias="v13_0",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


