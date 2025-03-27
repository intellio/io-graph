from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationError(BaseModel):
	code: Optional[str] = Field(alias="code", default=None,)
	message: Optional[str] = Field(alias="message", default=None,)
	tenantActionable: Optional[bool] = Field(alias="tenantActionable", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


