from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessPrivateAccessDetails(BaseModel):
	accessType: Optional[NetworkaccessAccessType | str] = Field(alias="accessType",default=None,)
	appSegmentId: Optional[str] = Field(alias="appSegmentId",default=None,)
	connectionStatus: Optional[NetworkaccessConnectionStatus | str] = Field(alias="connectionStatus",default=None,)
	connectorId: Optional[str] = Field(alias="connectorId",default=None,)
	connectorIp: Optional[str] = Field(alias="connectorIp",default=None,)
	connectorName: Optional[str] = Field(alias="connectorName",default=None,)
	processingRegion: Optional[str] = Field(alias="processingRegion",default=None,)
	thirdPartyTokenDetails: Optional[NetworkaccessThirdPartyTokenDetails] = Field(alias="thirdPartyTokenDetails",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .networkaccess_access_type import NetworkaccessAccessType
from .networkaccess_connection_status import NetworkaccessConnectionStatus
from .networkaccess_third_party_token_details import NetworkaccessThirdPartyTokenDetails

