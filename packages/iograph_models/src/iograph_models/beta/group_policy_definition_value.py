from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyDefinitionValue(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	configurationType: Optional[GroupPolicyConfigurationType | str] = Field(alias="configurationType",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	enabled: Optional[bool] = Field(alias="enabled",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	definition: Optional[GroupPolicyDefinition] = Field(alias="definition",default=None,)
	presentationValues: SerializeAsAny[Optional[list[GroupPolicyPresentationValue]]] = Field(alias="presentationValues",default=None,)

from .group_policy_configuration_type import GroupPolicyConfigurationType
from .group_policy_definition import GroupPolicyDefinition
from .group_policy_presentation_value import GroupPolicyPresentationValue

