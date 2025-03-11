from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedAppDiagnosticStatus(BaseModel):
	mitigationInstruction: Optional[str] = Field(alias="mitigationInstruction",default=None,)
	state: Optional[str] = Field(alias="state",default=None,)
	validationName: Optional[str] = Field(alias="validationName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


