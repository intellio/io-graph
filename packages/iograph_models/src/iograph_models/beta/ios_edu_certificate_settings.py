from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosEduCertificateSettings(BaseModel):
	certFileName: Optional[str] = Field(alias="certFileName", default=None,)
	certificateTemplateName: Optional[str] = Field(alias="certificateTemplateName", default=None,)
	certificateValidityPeriodScale: Optional[CertificateValidityPeriodScale | str] = Field(alias="certificateValidityPeriodScale", default=None,)
	certificateValidityPeriodValue: Optional[int] = Field(alias="certificateValidityPeriodValue", default=None,)
	certificationAuthority: Optional[str] = Field(alias="certificationAuthority", default=None,)
	certificationAuthorityName: Optional[str] = Field(alias="certificationAuthorityName", default=None,)
	renewalThresholdPercentage: Optional[int] = Field(alias="renewalThresholdPercentage", default=None,)
	trustedRootCertificate: Optional[str] = Field(alias="trustedRootCertificate", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .certificate_validity_period_scale import CertificateValidityPeriodScale
