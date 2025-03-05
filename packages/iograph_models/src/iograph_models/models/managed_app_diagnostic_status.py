from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedAppDiagnosticStatus(BaseModel):
	mitigationInstruction: Optional[str] = Field(default=None,alias="mitigationInstruction",)
	state: Optional[str] = Field(default=None,alias="state",)
	validationName: Optional[str] = Field(default=None,alias="validationName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


