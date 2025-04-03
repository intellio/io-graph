from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PublicKeyInfrastructureRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.publicKeyInfrastructureRoot"] = Field(alias="@odata.type", default="#microsoft.graph.publicKeyInfrastructureRoot")
	certificateBasedAuthConfigurations: Optional[list[CertificateBasedAuthPki]] = Field(alias="certificateBasedAuthConfigurations", default=None,)

from .certificate_based_auth_pki import CertificateBasedAuthPki
