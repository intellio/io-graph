from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InvestigationSecurityState(BaseModel):
	name: Optional[str] = Field(default=None,alias="name",)
	status: Optional[str] = Field(default=None,alias="status",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


