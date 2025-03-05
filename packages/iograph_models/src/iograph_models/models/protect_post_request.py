from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ProtectPostRequest(BaseModel):
	options: Optional[WorkbookWorksheetProtectionOptions] = Field(default=None,alias="options",)

from .workbook_worksheet_protection_options import WorkbookWorksheetProtectionOptions

