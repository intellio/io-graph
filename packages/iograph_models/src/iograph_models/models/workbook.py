from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Workbook(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	application: Optional[WorkbookApplication] = Field(default=None,alias="application",)
	comments: list[WorkbookComment] = Field(alias="comments",)
	functions: Optional[WorkbookFunctions] = Field(default=None,alias="functions",)
	names: list[WorkbookNamedItem] = Field(alias="names",)
	operations: list[WorkbookOperation] = Field(alias="operations",)
	tables: list[WorkbookTable] = Field(alias="tables",)
	worksheets: list[WorkbookWorksheet] = Field(alias="worksheets",)

from .workbook_application import WorkbookApplication
from .workbook_comment import WorkbookComment
from .workbook_functions import WorkbookFunctions
from .workbook_named_item import WorkbookNamedItem
from .workbook_operation import WorkbookOperation
from .workbook_table import WorkbookTable
from .workbook_worksheet import WorkbookWorksheet

