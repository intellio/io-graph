from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_source_imagesGetResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[CloudPcSourceDeviceImage]] = Field(default=None,alias="value",)

from .cloud_pc_source_device_image import CloudPcSourceDeviceImage

