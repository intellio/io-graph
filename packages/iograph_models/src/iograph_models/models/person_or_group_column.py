from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PersonOrGroupColumn(BaseModel):
	allowMultipleSelection: Optional[bool] = Field(alias="allowMultipleSelection",default=None,)
	chooseFromType: Optional[str] = Field(alias="chooseFromType",default=None,)
	displayAs: Optional[str] = Field(alias="displayAs",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


