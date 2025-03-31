from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ServiceNowConnection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.serviceNowConnection"] = Field(alias="@odata.type",)
	authenticationMethod: Optional[Union[ServiceNowOauthSecretAuthentication]] = Field(alias="authenticationMethod", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	incidentApiUrl: Optional[str] = Field(alias="incidentApiUrl", default=None,)
	instanceUrl: Optional[str] = Field(alias="instanceUrl", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	lastQueriedDateTime: Optional[datetime] = Field(alias="lastQueriedDateTime", default=None,)
	serviceNowConnectionStatus: Optional[ServiceNowConnectionStatus | str] = Field(alias="serviceNowConnectionStatus", default=None,)

from .service_now_oauth_secret_authentication import ServiceNowOauthSecretAuthentication
from .service_now_connection_status import ServiceNowConnectionStatus
