from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class NetworkaccessRelatedResourceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[NetworkaccessRelatedDestination, NetworkaccessRelatedDevice, NetworkaccessRelatedFile, NetworkaccessRelatedFileHash, NetworkaccessRelatedMalware, NetworkaccessRelatedRemoteNetwork, NetworkaccessRelatedTenant, NetworkaccessRelatedThreatIntelligence, NetworkaccessRelatedToken, NetworkaccessRelatedTransaction, NetworkaccessRelatedUrl, NetworkaccessRelatedUser, NetworkaccessRelatedWebCategory],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .networkaccess_related_destination import NetworkaccessRelatedDestination
from .networkaccess_related_device import NetworkaccessRelatedDevice
from .networkaccess_related_file import NetworkaccessRelatedFile
from .networkaccess_related_file_hash import NetworkaccessRelatedFileHash
from .networkaccess_related_malware import NetworkaccessRelatedMalware
from .networkaccess_related_remote_network import NetworkaccessRelatedRemoteNetwork
from .networkaccess_related_tenant import NetworkaccessRelatedTenant
from .networkaccess_related_threat_intelligence import NetworkaccessRelatedThreatIntelligence
from .networkaccess_related_token import NetworkaccessRelatedToken
from .networkaccess_related_transaction import NetworkaccessRelatedTransaction
from .networkaccess_related_url import NetworkaccessRelatedUrl
from .networkaccess_related_user import NetworkaccessRelatedUser
from .networkaccess_related_web_category import NetworkaccessRelatedWebCategory
