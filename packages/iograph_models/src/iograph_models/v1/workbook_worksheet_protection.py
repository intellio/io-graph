from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookWorksheetProtection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	options: Optional[WorkbookWorksheetProtectionOptions] = Field(alias="options", default=None,)
	protected: Optional[bool] = Field(alias="protected", default=None,)

from .workbook_worksheet_protection_options import WorkbookWorksheetProtectionOptions

