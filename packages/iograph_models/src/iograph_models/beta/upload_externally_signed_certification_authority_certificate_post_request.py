from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Upload_externally_signed_certification_authority_certificatePostRequest(BaseModel):
	signedCertificate: Optional[str] = Field(alias="signedCertificate", default=None,)
	trustChainCertificates: Optional[list[TrustChainCertificate]] = Field(alias="trustChainCertificates", default=None,)
	certificationAuthorityVersion: Optional[int] = Field(alias="certificationAuthorityVersion", default=None,)

from .trust_chain_certificate import TrustChainCertificate
