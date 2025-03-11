from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDetonationDetails(BaseModel):
	analysisDateTime: Optional[datetime] = Field(alias="analysisDateTime",default=None,)
	compromiseIndicators: Optional[list[SecurityCompromiseIndicator]] = Field(alias="compromiseIndicators",default=None,)
	detonationBehaviourDetails: Optional[SecurityDetonationBehaviourDetails] = Field(alias="detonationBehaviourDetails",default=None,)
	detonationChain: Optional[SecurityDetonationChain] = Field(alias="detonationChain",default=None,)
	detonationObservables: Optional[SecurityDetonationObservables] = Field(alias="detonationObservables",default=None,)
	detonationScreenshotUri: Optional[str] = Field(alias="detonationScreenshotUri",default=None,)
	detonationVerdict: Optional[str] = Field(alias="detonationVerdict",default=None,)
	detonationVerdictReason: Optional[str] = Field(alias="detonationVerdictReason",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .security_compromise_indicator import SecurityCompromiseIndicator
from .security_detonation_behaviour_details import SecurityDetonationBehaviourDetails
from .security_detonation_chain import SecurityDetonationChain
from .security_detonation_observables import SecurityDetonationObservables

