from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DriveItemSource(BaseModel):
	application: Optional[DriveItemSourceApplication] = Field(default=None,alias="application",)
	externalId: Optional[str] = Field(default=None,alias="externalId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .drive_item_source_application import DriveItemSourceApplication

