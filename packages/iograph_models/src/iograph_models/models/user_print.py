from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserPrint(BaseModel):
	recentPrinterShares: Optional[list[PrinterShare]] = Field(default=None,alias="recentPrinterShares",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .printer_share import PrinterShare

