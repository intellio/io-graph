from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MatrixChoiceAnswer(BaseModel):
	displayText: Optional[str] = Field(alias="displayText", default=None,)
	key: Optional[str] = Field(alias="key", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


