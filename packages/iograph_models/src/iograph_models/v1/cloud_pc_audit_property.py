from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcAuditProperty(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	newValue: Optional[str] = Field(alias="newValue",default=None,)
	oldValue: Optional[str] = Field(alias="oldValue",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


