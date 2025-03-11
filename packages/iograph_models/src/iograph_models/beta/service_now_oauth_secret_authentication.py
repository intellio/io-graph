from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceNowOauthSecretAuthentication(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appId: Optional[str] = Field(alias="appId",default=None,)


