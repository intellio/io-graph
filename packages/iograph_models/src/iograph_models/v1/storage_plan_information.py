from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class StoragePlanInformation(BaseModel):
	upgradeAvailable: Optional[bool] = Field(alias="upgradeAvailable", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


