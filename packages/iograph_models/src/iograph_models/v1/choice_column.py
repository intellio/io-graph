from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChoiceColumn(BaseModel):
	allowTextEntry: Optional[bool] = Field(alias="allowTextEntry",default=None,)
	choices: Optional[list[str]] = Field(alias="choices",default=None,)
	displayAs: Optional[str] = Field(alias="displayAs",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


