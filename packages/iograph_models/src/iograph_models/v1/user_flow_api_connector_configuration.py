from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserFlowApiConnectorConfiguration(BaseModel):
	postAttributeCollection: Optional[IdentityApiConnector] = Field(alias="postAttributeCollection", default=None,)
	postFederationSignup: Optional[IdentityApiConnector] = Field(alias="postFederationSignup", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .identity_api_connector import IdentityApiConnector
