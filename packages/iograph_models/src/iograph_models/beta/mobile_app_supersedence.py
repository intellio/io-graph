from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppSupersedence(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	sourceDisplayName: Optional[str] = Field(alias="sourceDisplayName",default=None,)
	sourceDisplayVersion: Optional[str] = Field(alias="sourceDisplayVersion",default=None,)
	sourceId: Optional[str] = Field(alias="sourceId",default=None,)
	sourcePublisherDisplayName: Optional[str] = Field(alias="sourcePublisherDisplayName",default=None,)
	targetDisplayName: Optional[str] = Field(alias="targetDisplayName",default=None,)
	targetDisplayVersion: Optional[str] = Field(alias="targetDisplayVersion",default=None,)
	targetId: Optional[str] = Field(alias="targetId",default=None,)
	targetPublisher: Optional[str] = Field(alias="targetPublisher",default=None,)
	targetPublisherDisplayName: Optional[str] = Field(alias="targetPublisherDisplayName",default=None,)
	targetType: Optional[MobileAppRelationshipType | str] = Field(alias="targetType",default=None,)
	supersededAppCount: Optional[int] = Field(alias="supersededAppCount",default=None,)
	supersedenceType: Optional[MobileAppSupersedenceType | str] = Field(alias="supersedenceType",default=None,)
	supersedingAppCount: Optional[int] = Field(alias="supersedingAppCount",default=None,)

from .mobile_app_relationship_type import MobileAppRelationshipType
from .mobile_app_supersedence_type import MobileAppSupersedenceType

