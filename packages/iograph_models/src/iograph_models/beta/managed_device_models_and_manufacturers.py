from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedDeviceModelsAndManufacturers(BaseModel):
	deviceManufacturers: Optional[list[str]] = Field(alias="deviceManufacturers",default=None,)
	deviceModels: Optional[list[str]] = Field(alias="deviceModels",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


