from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppDependency(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.mobileAppDependency"] = Field(alias="@odata.type", default="#microsoft.graph.mobileAppDependency")
	sourceDisplayName: Optional[str] = Field(alias="sourceDisplayName", default=None,)
	sourceDisplayVersion: Optional[str] = Field(alias="sourceDisplayVersion", default=None,)
	sourceId: Optional[str] = Field(alias="sourceId", default=None,)
	sourcePublisherDisplayName: Optional[str] = Field(alias="sourcePublisherDisplayName", default=None,)
	targetDisplayName: Optional[str] = Field(alias="targetDisplayName", default=None,)
	targetDisplayVersion: Optional[str] = Field(alias="targetDisplayVersion", default=None,)
	targetId: Optional[str] = Field(alias="targetId", default=None,)
	targetPublisher: Optional[str] = Field(alias="targetPublisher", default=None,)
	targetPublisherDisplayName: Optional[str] = Field(alias="targetPublisherDisplayName", default=None,)
	targetType: Optional[MobileAppRelationshipType | str] = Field(alias="targetType", default=None,)
	dependencyType: Optional[MobileAppDependencyType | str] = Field(alias="dependencyType", default=None,)
	dependentAppCount: Optional[int] = Field(alias="dependentAppCount", default=None,)
	dependsOnAppCount: Optional[int] = Field(alias="dependsOnAppCount", default=None,)

from .mobile_app_relationship_type import MobileAppRelationshipType
from .mobile_app_dependency_type import MobileAppDependencyType

