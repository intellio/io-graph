from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Quota(BaseModel):
	deleted: Optional[int] = Field(alias="deleted", default=None,)
	remaining: Optional[int] = Field(alias="remaining", default=None,)
	state: Optional[str] = Field(alias="state", default=None,)
	storagePlanInformation: Optional[StoragePlanInformation] = Field(alias="storagePlanInformation", default=None,)
	total: Optional[int] = Field(alias="total", default=None,)
	used: Optional[int] = Field(alias="used", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .storage_plan_information import StoragePlanInformation

