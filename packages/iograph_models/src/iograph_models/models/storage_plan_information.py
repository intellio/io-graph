from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class StoragePlanInformation(BaseModel):
	upgradeAvailable: Optional[bool] = Field(default=None,alias="upgradeAvailable",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


