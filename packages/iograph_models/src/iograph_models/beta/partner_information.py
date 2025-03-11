from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PartnerInformation(BaseModel):
	commerceUrl: Optional[str] = Field(alias="commerceUrl",default=None,)
	companyName: Optional[str] = Field(alias="companyName",default=None,)
	companyType: Optional[PartnerTenantType | str] = Field(alias="companyType",default=None,)
	helpUrl: Optional[str] = Field(alias="helpUrl",default=None,)
	partnerTenantId: Optional[str] = Field(alias="partnerTenantId",default=None,)
	supportEmails: Optional[list[str]] = Field(alias="supportEmails",default=None,)
	supportTelephones: Optional[list[str]] = Field(alias="supportTelephones",default=None,)
	supportUrl: Optional[str] = Field(alias="supportUrl",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .partner_tenant_type import PartnerTenantType

