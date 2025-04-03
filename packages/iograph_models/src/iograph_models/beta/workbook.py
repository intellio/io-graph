from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Workbook(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbook"] = Field(alias="@odata.type", default="#microsoft.graph.workbook")
	application: Optional[WorkbookApplication] = Field(alias="application", default=None,)
	comments: Optional[list[WorkbookComment]] = Field(alias="comments", default=None,)
	functions: Optional[WorkbookFunctions] = Field(alias="functions", default=None,)
	names: Optional[list[WorkbookNamedItem]] = Field(alias="names", default=None,)
	operations: Optional[list[WorkbookOperation]] = Field(alias="operations", default=None,)
	tables: Optional[list[WorkbookTable]] = Field(alias="tables", default=None,)
	worksheets: Optional[list[WorkbookWorksheet]] = Field(alias="worksheets", default=None,)

from .workbook_application import WorkbookApplication
from .workbook_comment import WorkbookComment
from .workbook_functions import WorkbookFunctions
from .workbook_named_item import WorkbookNamedItem
from .workbook_operation import WorkbookOperation
from .workbook_table import WorkbookTable
from .workbook_worksheet import WorkbookWorksheet
