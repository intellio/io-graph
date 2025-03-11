from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityProviderStatus(BaseModel):
	enabled: Optional[bool] = Field(alias="enabled",default=None,)
	endpoint: Optional[str] = Field(alias="endpoint",default=None,)
	provider: Optional[str] = Field(alias="provider",default=None,)
	region: Optional[str] = Field(alias="region",default=None,)
	vendor: Optional[str] = Field(alias="vendor",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


