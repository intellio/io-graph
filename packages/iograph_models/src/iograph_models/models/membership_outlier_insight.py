from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MembershipOutlierInsight(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	insightCreatedDateTime: Optional[datetime] = Field(default=None,alias="insightCreatedDateTime",)
	containerId: Optional[str] = Field(default=None,alias="containerId",)
	memberId: Optional[str] = Field(default=None,alias="memberId",)
	outlierContainerType: Optional[OutlierContainerType] = Field(default=None,alias="outlierContainerType",)
	outlierMemberType: Optional[OutlierMemberType] = Field(default=None,alias="outlierMemberType",)
	container: Optional[DirectoryObject] = Field(default=None,alias="container",)
	lastModifiedBy: Optional[User] = Field(default=None,alias="lastModifiedBy",)
	member: Optional[DirectoryObject] = Field(default=None,alias="member",)

from .outlier_container_type import OutlierContainerType
from .outlier_member_type import OutlierMemberType
from .directory_object import DirectoryObject
from .user import User
from .directory_object import DirectoryObject

