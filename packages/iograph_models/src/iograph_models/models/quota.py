from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Quota(BaseModel):
	deleted: Optional[int] = Field(default=None,alias="deleted",)
	remaining: Optional[int] = Field(default=None,alias="remaining",)
	state: Optional[str] = Field(default=None,alias="state",)
	storagePlanInformation: Optional[StoragePlanInformation] = Field(default=None,alias="storagePlanInformation",)
	total: Optional[int] = Field(default=None,alias="total",)
	used: Optional[int] = Field(default=None,alias="used",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .storage_plan_information import StoragePlanInformation

