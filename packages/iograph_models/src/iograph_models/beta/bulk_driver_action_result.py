from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BulkDriverActionResult(BaseModel):
	failedDriverIds: Optional[list[str]] = Field(alias="failedDriverIds", default=None,)
	notFoundDriverIds: Optional[list[str]] = Field(alias="notFoundDriverIds", default=None,)
	successfulDriverIds: Optional[list[str]] = Field(alias="successfulDriverIds", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


