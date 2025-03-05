from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Workbook(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	application: Optional[WorkbookApplication] = Field(default=None,alias="application",)
	comments: Optional[list[WorkbookComment]] = Field(default=None,alias="comments",)
	functions: Optional[WorkbookFunctions] = Field(default=None,alias="functions",)
	names: Optional[list[WorkbookNamedItem]] = Field(default=None,alias="names",)
	operations: Optional[list[WorkbookOperation]] = Field(default=None,alias="operations",)
	tables: Optional[list[WorkbookTable]] = Field(default=None,alias="tables",)
	worksheets: Optional[list[WorkbookWorksheet]] = Field(default=None,alias="worksheets",)

from .workbook_application import WorkbookApplication
from .workbook_comment import WorkbookComment
from .workbook_functions import WorkbookFunctions
from .workbook_named_item import WorkbookNamedItem
from .workbook_operation import WorkbookOperation
from .workbook_table import WorkbookTable
from .workbook_worksheet import WorkbookWorksheet

