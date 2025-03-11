from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrintSettings(BaseModel):
	documentConversionEnabled: Optional[bool] = Field(alias="documentConversionEnabled",default=None,)
	printerDiscoverySettings: Optional[PrinterDiscoverySettings] = Field(alias="printerDiscoverySettings",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .printer_discovery_settings import PrinterDiscoverySettings

