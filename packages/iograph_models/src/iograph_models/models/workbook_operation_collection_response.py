from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[WorkbookOperation]] = Field(alias="value",default=None,)

from .workbook_operation import WorkbookOperation

