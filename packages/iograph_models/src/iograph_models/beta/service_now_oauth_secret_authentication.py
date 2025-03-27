from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceNowOauthSecretAuthentication(BaseModel):
	odata_type: Literal["#microsoft.graph.serviceNowOauthSecretAuthentication"] = Field(alias="@odata.type", default="#microsoft.graph.serviceNowOauthSecretAuthentication")
	appId: Optional[str] = Field(alias="appId", default=None,)


