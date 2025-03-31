from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookWorksheetProtection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookWorksheetProtection"] = Field(alias="@odata.type",)
	options: Optional[WorkbookWorksheetProtectionOptions] = Field(alias="options", default=None,)
	protected: Optional[bool] = Field(alias="protected", default=None,)

from .workbook_worksheet_protection_options import WorkbookWorksheetProtectionOptions
