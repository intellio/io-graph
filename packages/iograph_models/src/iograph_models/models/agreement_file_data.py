from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AgreementFileData(BaseModel):
	data: Optional[str] = Field(default=None,alias="data",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


