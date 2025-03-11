from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PublicKeyInfrastructureRoot(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	certificateBasedAuthConfigurations: Optional[list[CertificateBasedAuthPki]] = Field(alias="certificateBasedAuthConfigurations",default=None,)

from .certificate_based_auth_pki import CertificateBasedAuthPki

