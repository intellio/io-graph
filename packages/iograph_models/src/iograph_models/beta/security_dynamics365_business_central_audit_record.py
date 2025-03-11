from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDynamics365BusinessCentralAuditRecord(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


