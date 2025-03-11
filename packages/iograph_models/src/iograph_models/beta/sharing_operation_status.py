from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SharingOperationStatus(BaseModel):
	disabledReason: Optional[str] = Field(alias="disabledReason",default=None,)
	enabled: Optional[bool] = Field(alias="enabled",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


