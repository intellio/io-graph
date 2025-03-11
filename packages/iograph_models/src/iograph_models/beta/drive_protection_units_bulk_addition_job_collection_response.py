from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DriveProtectionUnitsBulkAdditionJobCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[DriveProtectionUnitsBulkAdditionJob]] = Field(alias="value",default=None,)

from .drive_protection_units_bulk_addition_job import DriveProtectionUnitsBulkAdditionJob

