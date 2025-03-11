from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CertificateAuthorityPath(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	certificateBasedApplicationConfigurations: Optional[list[CertificateBasedApplicationConfiguration]] = Field(alias="certificateBasedApplicationConfigurations",default=None,)
	mutualTlsOauthConfigurations: Optional[list[MutualTlsOauthConfiguration]] = Field(alias="mutualTlsOauthConfigurations",default=None,)

from .certificate_based_application_configuration import CertificateBasedApplicationConfiguration
from .mutual_tls_oauth_configuration import MutualTlsOauthConfiguration

