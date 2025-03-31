from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ProtectPostRequest(BaseModel):
	options: Optional[WorkbookWorksheetProtectionOptions] = Field(alias="options", default=None,)

from .workbook_worksheet_protection_options import WorkbookWorksheetProtectionOptions
