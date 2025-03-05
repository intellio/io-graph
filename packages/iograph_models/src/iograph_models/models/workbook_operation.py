from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	error: Optional[WorkbookOperationError] = Field(default=None,alias="error",)
	resourceLocation: Optional[str] = Field(default=None,alias="resourceLocation",)
	status: Optional[WorkbookOperationStatus] = Field(default=None,alias="status",)

from .workbook_operation_error import WorkbookOperationError
from .workbook_operation_status import WorkbookOperationStatus

