from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkTeamsClientConfiguration(BaseModel):
	accountConfiguration: Optional[TeamworkAccountConfiguration] = Field(alias="accountConfiguration",default=None,)
	featuresConfiguration: Optional[TeamworkFeaturesConfiguration] = Field(alias="featuresConfiguration",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .teamwork_account_configuration import TeamworkAccountConfiguration
from .teamwork_features_configuration import TeamworkFeaturesConfiguration

