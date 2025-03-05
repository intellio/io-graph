from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookOperation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	error: Optional[WorkbookOperationError] = Field(alias="error",default=None,)
	resourceLocation: Optional[str] = Field(alias="resourceLocation",default=None,)
	status: Optional[str | WorkbookOperationStatus] = Field(alias="status",default=None,)

from .workbook_operation_error import WorkbookOperationError
from .workbook_operation_status import WorkbookOperationStatus

