from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessAlert(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	actions: Optional[list[NetworkaccessAlertAction]] = Field(alias="actions",default=None,)
	alertType: Optional[NetworkaccessAlertType | str] = Field(alias="alertType",default=None,)
	creationDateTime: Optional[datetime] = Field(alias="creationDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	detectionTechnology: Optional[str] = Field(alias="detectionTechnology",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	relatedResources: SerializeAsAny[Optional[list[NetworkaccessRelatedResource]]] = Field(alias="relatedResources",default=None,)
	severity: Optional[NetworkaccessAlertSeverity | str] = Field(alias="severity",default=None,)
	vendorName: Optional[str] = Field(alias="vendorName",default=None,)
	policy: Optional[NetworkaccessFilteringPolicy] = Field(alias="policy",default=None,)

from .networkaccess_alert_action import NetworkaccessAlertAction
from .networkaccess_alert_type import NetworkaccessAlertType
from .networkaccess_related_resource import NetworkaccessRelatedResource
from .networkaccess_alert_severity import NetworkaccessAlertSeverity
from .networkaccess_filtering_policy import NetworkaccessFilteringPolicy

