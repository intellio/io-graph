from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookOperation"] = Field(alias="@odata.type",)
	error: Optional[WorkbookOperationError] = Field(alias="error", default=None,)
	resourceLocation: Optional[str] = Field(alias="resourceLocation", default=None,)
	status: Optional[WorkbookOperationStatus | str] = Field(alias="status", default=None,)

from .workbook_operation_error import WorkbookOperationError
from .workbook_operation_status import WorkbookOperationStatus
