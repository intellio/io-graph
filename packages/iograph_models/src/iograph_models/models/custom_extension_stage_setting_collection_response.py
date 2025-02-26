from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CustomExtensionStageSettingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[CustomExtensionStageSetting] = Field(alias="value",)

from .custom_extension_stage_setting import CustomExtensionStageSetting

