from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DriveItemSource(BaseModel):
	application: Optional[DriveItemSourceApplication | str] = Field(alias="application", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .drive_item_source_application import DriveItemSourceApplication
