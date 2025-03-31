from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcPartnerAgentInstallResult(BaseModel):
	errorMessage: Optional[str] = Field(alias="errorMessage", default=None,)
	installStatus: Optional[CloudPcPartnerAgentInstallStatus | str] = Field(alias="installStatus", default=None,)
	isThirdPartyPartner: Optional[bool] = Field(alias="isThirdPartyPartner", default=None,)
	partnerAgentName: Optional[CloudPcPartnerAgentName | str] = Field(alias="partnerAgentName", default=None,)
	retriable: Optional[bool] = Field(alias="retriable", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .cloud_pc_partner_agent_install_status import CloudPcPartnerAgentInstallStatus
from .cloud_pc_partner_agent_name import CloudPcPartnerAgentName
