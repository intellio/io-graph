from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class GroupPolicyDefinitionValue(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.groupPolicyDefinitionValue"] = Field(alias="@odata.type",)
	configurationType: Optional[GroupPolicyConfigurationType | str] = Field(alias="configurationType", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	enabled: Optional[bool] = Field(alias="enabled", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	definition: Optional[GroupPolicyDefinition] = Field(alias="definition", default=None,)
	presentationValues: Optional[list[Annotated[Union[GroupPolicyPresentationValueBoolean, GroupPolicyPresentationValueDecimal, GroupPolicyPresentationValueList, GroupPolicyPresentationValueLongDecimal, GroupPolicyPresentationValueMultiText, GroupPolicyPresentationValueText],Field(discriminator="odata_type")]]] = Field(alias="presentationValues", default=None,)

from .group_policy_configuration_type import GroupPolicyConfigurationType
from .group_policy_definition import GroupPolicyDefinition
from .group_policy_presentation_value_boolean import GroupPolicyPresentationValueBoolean
from .group_policy_presentation_value_decimal import GroupPolicyPresentationValueDecimal
from .group_policy_presentation_value_list import GroupPolicyPresentationValueList
from .group_policy_presentation_value_long_decimal import GroupPolicyPresentationValueLongDecimal
from .group_policy_presentation_value_multi_text import GroupPolicyPresentationValueMultiText
from .group_policy_presentation_value_text import GroupPolicyPresentationValueText
