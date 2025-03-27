from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessAlert(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	actions: Optional[list[NetworkaccessAlertAction]] = Field(alias="actions", default=None,)
	alertType: Optional[NetworkaccessAlertType | str] = Field(alias="alertType", default=None,)
	creationDateTime: Optional[datetime] = Field(alias="creationDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	detectionTechnology: Optional[str] = Field(alias="detectionTechnology", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	relatedResources: Optional[list[Annotated[Union[NetworkaccessRelatedDestination, NetworkaccessRelatedDevice, NetworkaccessRelatedFile, NetworkaccessRelatedFileHash, NetworkaccessRelatedMalware, NetworkaccessRelatedRemoteNetwork, NetworkaccessRelatedTenant, NetworkaccessRelatedThreatIntelligence, NetworkaccessRelatedToken, NetworkaccessRelatedTransaction, NetworkaccessRelatedUrl, NetworkaccessRelatedUser, NetworkaccessRelatedWebCategory],Field(discriminator="odata_type")]]] = Field(alias="relatedResources", default=None,)
	severity: Optional[NetworkaccessAlertSeverity | str] = Field(alias="severity", default=None,)
	vendorName: Optional[str] = Field(alias="vendorName", default=None,)
	policy: Optional[NetworkaccessFilteringPolicy] = Field(alias="policy", default=None,)

from .networkaccess_alert_action import NetworkaccessAlertAction
from .networkaccess_alert_type import NetworkaccessAlertType
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
from .networkaccess_alert_severity import NetworkaccessAlertSeverity
from .networkaccess_filtering_policy import NetworkaccessFilteringPolicy

