from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserFlowApiConnectorConfiguration(BaseModel):
	postAttributeCollection: Optional[IdentityApiConnector] = Field(default=None,alias="postAttributeCollection",)
	postFederationSignup: Optional[IdentityApiConnector] = Field(default=None,alias="postFederationSignup",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_api_connector import IdentityApiConnector
from .identity_api_connector import IdentityApiConnector

