from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LookupColumn(BaseModel):
	allowMultipleValues: Optional[bool] = Field(alias="allowMultipleValues",default=None,)
	allowUnlimitedLength: Optional[bool] = Field(alias="allowUnlimitedLength",default=None,)
	columnName: Optional[str] = Field(alias="columnName",default=None,)
	listId: Optional[str] = Field(alias="listId",default=None,)
	primaryLookupColumnId: Optional[str] = Field(alias="primaryLookupColumnId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


