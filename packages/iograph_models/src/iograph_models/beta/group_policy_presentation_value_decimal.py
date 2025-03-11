from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyPresentationValueDecimal(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	definitionValue: Optional[GroupPolicyDefinitionValue] = Field(alias="definitionValue",default=None,)
	presentation: SerializeAsAny[Optional[GroupPolicyPresentation]] = Field(alias="presentation",default=None,)
	value: Optional[int] = Field(alias="value",default=None,)

from .group_policy_definition_value import GroupPolicyDefinitionValue
from .group_policy_presentation import GroupPolicyPresentation

