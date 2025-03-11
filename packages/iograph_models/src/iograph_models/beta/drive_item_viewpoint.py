from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DriveItemViewpoint(BaseModel):
	accessOperations: Optional[DriveItemAccessOperationsViewpoint] = Field(alias="accessOperations",default=None,)
	sharing: Optional[SharingViewpoint] = Field(alias="sharing",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .drive_item_access_operations_viewpoint import DriveItemAccessOperationsViewpoint
from .sharing_viewpoint import SharingViewpoint

