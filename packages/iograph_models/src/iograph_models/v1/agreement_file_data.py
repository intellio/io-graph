from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AgreementFileData(BaseModel):
	data: Optional[str] = Field(alias="data", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

