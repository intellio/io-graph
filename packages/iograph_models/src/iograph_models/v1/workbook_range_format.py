from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookRangeFormat(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	columnWidth: float | str | ReferenceNumeric
	horizontalAlignment: Optional[str] = Field(alias="horizontalAlignment", default=None,)
	rowHeight: float | str | ReferenceNumeric
	verticalAlignment: Optional[str] = Field(alias="verticalAlignment", default=None,)
	wrapText: Optional[bool] = Field(alias="wrapText", default=None,)
	borders: Optional[list[WorkbookRangeBorder]] = Field(alias="borders", default=None,)
	fill: Optional[WorkbookRangeFill] = Field(alias="fill", default=None,)
	font: Optional[WorkbookRangeFont] = Field(alias="font", default=None,)
	protection: Optional[WorkbookFormatProtection] = Field(alias="protection", default=None,)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .workbook_range_border import WorkbookRangeBorder
from .workbook_range_fill import WorkbookRangeFill
from .workbook_range_font import WorkbookRangeFont
from .workbook_format_protection import WorkbookFormatProtection

