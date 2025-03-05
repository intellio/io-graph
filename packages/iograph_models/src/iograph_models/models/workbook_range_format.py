from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookRangeFormat(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	columnWidth: float | str | ReferenceNumeric
	horizontalAlignment: Optional[str] = Field(default=None,alias="horizontalAlignment",)
	rowHeight: float | str | ReferenceNumeric
	verticalAlignment: Optional[str] = Field(default=None,alias="verticalAlignment",)
	wrapText: Optional[bool] = Field(default=None,alias="wrapText",)
	borders: Optional[list[WorkbookRangeBorder]] = Field(default=None,alias="borders",)
	fill: Optional[WorkbookRangeFill] = Field(default=None,alias="fill",)
	font: Optional[WorkbookRangeFont] = Field(default=None,alias="font",)
	protection: Optional[WorkbookFormatProtection] = Field(default=None,alias="protection",)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .workbook_range_border import WorkbookRangeBorder
from .workbook_range_fill import WorkbookRangeFill
from .workbook_range_font import WorkbookRangeFont
from .workbook_format_protection import WorkbookFormatProtection

