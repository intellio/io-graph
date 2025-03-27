from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AirPrintSettings(BaseModel):
	incompatiblePrinters: Optional[IncompatiblePrinterSettings | str] = Field(alias="incompatiblePrinters", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .incompatible_printer_settings import IncompatiblePrinterSettings

