from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ProviderTenantSetting(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	azureTenantId: Optional[str] = Field(alias="azureTenantId",default=None,)
	enabled: Optional[bool] = Field(alias="enabled",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	provider: Optional[str] = Field(alias="provider",default=None,)
	vendor: Optional[str] = Field(alias="vendor",default=None,)


