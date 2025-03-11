from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrinterDiscoverySettings(BaseModel):
	airPrint: Optional[AirPrintSettings] = Field(alias="airPrint",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .air_print_settings import AirPrintSettings

