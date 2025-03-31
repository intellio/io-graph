from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class IdentityApiConnector(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.identityApiConnector"] = Field(alias="@odata.type",)
	authenticationConfiguration: Optional[Union[BasicAuthentication, ClientCertificateAuthentication, Pkcs12Certificate]] = Field(alias="authenticationConfiguration", default=None,discriminator="odata_type", )
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	targetUrl: Optional[str] = Field(alias="targetUrl", default=None,)

from .basic_authentication import BasicAuthentication
from .client_certificate_authentication import ClientCertificateAuthentication
from .pkcs12_certificate import Pkcs12Certificate
