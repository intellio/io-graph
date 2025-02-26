from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcUserSettingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[CloudPcUserSetting] = Field(alias="value",)

from .cloud_pc_user_setting import CloudPcUserSetting

