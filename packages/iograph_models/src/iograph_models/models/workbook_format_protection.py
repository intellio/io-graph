from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookFormatProtection(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	formulaHidden: Optional[bool] = Field(default=None,alias="formulaHidden",)
	locked: Optional[bool] = Field(default=None,alias="locked",)


