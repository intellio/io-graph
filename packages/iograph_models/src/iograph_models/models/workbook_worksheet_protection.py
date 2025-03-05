from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookWorksheetProtection(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	options: Optional[WorkbookWorksheetProtectionOptions] = Field(default=None,alias="options",)
	protected: Optional[bool] = Field(default=None,alias="protected",)

from .workbook_worksheet_protection_options import WorkbookWorksheetProtectionOptions

