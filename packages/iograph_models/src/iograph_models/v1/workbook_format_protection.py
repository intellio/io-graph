from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookFormatProtection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	formulaHidden: Optional[bool] = Field(alias="formulaHidden", default=None,)
	locked: Optional[bool] = Field(alias="locked", default=None,)


