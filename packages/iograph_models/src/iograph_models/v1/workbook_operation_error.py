from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookOperationError(BaseModel):
	code: Optional[str] = Field(alias="code",default=None,)
	innerError: Optional[WorkbookOperationError] = Field(alias="innerError",default=None,)
	message: Optional[str] = Field(alias="message",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


